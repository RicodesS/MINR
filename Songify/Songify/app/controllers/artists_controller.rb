require 'lastfm'
require 'httparty'

class ArtistsController < ApplicationController
    before_action :require_login
     respond_to :js, :json, :html


    def require_login
      unless current_user != nil
      flash[:error] =  "You require to login!"
        redirect_to new_user_session_path # halts request cycle
      end
    end

    def index
        @topArtists = show_top_artists
    end

    def star
        @topArtists = show_top_artists
        @star = params[:stars]
    end

    def rank
        @revec=''
        @arvec=''
        @topArtists = show_top_artists
        @topArtists.each do |artist|
            @arvec << artist['name']+'+'
            @revec << ArtistsController.get_avg(artist['name']).to_s+' '
        end
        @c = @revec.split(' ').zip(@arvec.split('+')).sort.reverse
    end

    def show
        @artists = show_top_artists
        @artist = get_artist_by_name(@artists,params[:id])
        @name = params[:id]
        @bio = get_artist_bio(params[:id])
        @id = get_id_by_name(params[:id])
        @topAlbums = get_top_albums_by_artist_name(params[:id])
        @topTracks = get_top_tracks_by_artist_name(params[:id])
        @similarArtists = get_similar_artists(params[:id])
        @tags = ArtistsController.get_tags(params[:id])
        @comments =Comment.all
        @val = Valuation.all
    end

public

def self.get_avg(name)
        @sum = 0.0
            @n = 0.0
            @val = Valuation.all
            @val.each do |val|
                if(val.artist ==  name)
                    @sum =@sum + val.value.to_f
                    @n=@n+1
                end
            end
            if @sum != 0.0
                @sum = @sum/@n
            end
            if @sum == 'NaN'
                return 0.to_i
            else
                return @sum
            end
    end

    def self.has_reviewed(user,name)
        @val = Valuation.all
        @val.each do |val|
            if val.user_id.to_i == user && val.artist.to_s == name
                return val
            end
        end
        return Valuation.new
    end

    def self.has_reported_comment(user,comment)
    @rep = Report.all
    @rep.each do |r|
      if r.user_id.to_i == user.to_i && r.comment.id.to_i == comment.to_i && !r.verif
        return true
      end
    end
    return false
end

   def self.has_reported_user(user,us)
    @rep = Report.all
    @rep.each do |r|
      if r.user_id.to_i == user.to_i && r.ut.to_i == us.to_i && r.verif
        return true
      end
    end
    return false
end
    def show_top_artists
        lastfm = Lastfm.new(ENV["LASTFM_API_KEY"], ENV["LASTFM_API_SECRET"])
        token = lastfm.auth.get_token
        return lastfm.chart.get_top_artists
    end

    private
    def get_artist_bio(name)
         lastfm = Lastfm.new(ENV["LASTFM_API_KEY"], ENV["LASTFM_API_SECRET"])
         token = lastfm.auth.get_token
         bio =  lastfm.artist.get_info(artist: name)
         return bio
    end

    private
    def get_artist_by_name(artists,name)
        artists.each do |artist|
            if(name == artist['name'])
                return artist
            end
        end
        render_not_found
    end

    private
    def get_id_by_name(name)
        response = HTTParty.get('https://api.songkick.com/api/3.0/search/artists.json?apikey='+ ENV['SONGKICK_API_KEY'] + '&query='+name+'')
        @resultsPage = JSON.parse(response.body)
        return @resultsPage["resultsPage"]["results"]["artist"][0]["id"]
    end

    private
    def get_top_albums_by_artist_name(name)
        lastfm = Lastfm.new(ENV["LASTFM_API_KEY"], ENV["LASTFM_API_SECRET"])
        token = lastfm.auth.get_token
        albums = lastfm.artist.get_top_albums(artist: name)
    end

    private
    def get_top_tracks_by_artist_name(name)
        lastfm = Lastfm.new(ENV["LASTFM_API_KEY"], ENV["LASTFM_API_SECRET"])
        token = lastfm.auth.get_token
        tracks = lastfm.artist.get_top_tracks(artist: name)
    end

    private
    def get_similar_artists(name)
        lastfm = Lastfm.new(ENV["LASTFM_API_KEY"], ENV["LASTFM_API_SECRET"])
        token = lastfm.auth.get_token
        tracks = lastfm.artist.get_similar(artist: name)
    end

    private
    def self.get_tags(name)
        lastfm = Lastfm.new(ENV["LASTFM_API_KEY"], ENV["LASTFM_API_SECRET"])
        token = lastfm.auth.get_token
        tracks = lastfm.artist.get_top_tags(artist: name)
    end

    private
    def render_not_found
        render :file => "#{Rails.root}/public/404.html",  :status => 404
    end


end
