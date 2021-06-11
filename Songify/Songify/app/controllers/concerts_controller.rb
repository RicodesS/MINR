require 'location'
require 'lastfm'
class ConcertsController < ApplicationController
    before_action :require_login

    def require_login
      unless current_user != nil
      flash[:error] =  "You require to login!"
        redirect_to new_user_session_path # halts request cycle
      end
    end

    remote = Songkickr::Remote.new ENV["SONGKICK_API_KEY"]
    @@results = remote.events(location: "clientip").results

    def index2
        @results = @@results
    end

    def index
        @results = @@results
    end

    def search
        @results = @@results
        @artists = show_top_artists
        @input = params[:search]
    end

    def searchDate
        @results = @@results
        @date = params[:date]
    end

    def searchZone
        @results = @@results
        @zone = params[:zone]
    end

    def show
        @events = @@results
        @event = search_id(@events, params[:id])
        my_loc = BingLocator.new()
        my_loc.api_key = 'AjCnyg3J-cQx0PfxOJd8GD_XYZqqba8-tNAem7JgPVd_LN0H-DY_TlwDzYktf4lt'
        @venue = get_venue_by_id(@event.venue.id)
        if(@event.venue.lat == nil && @event.venue.lat == nil)
            my_loc.query = @venue.metro_area.display_name
            @location = my_loc.get_img_url_by_query(600,300)
        else 
            my_loc.latitude = @event.venue.lat 
            my_loc.longitude = @event.venue.lng
            @location = my_loc.get_img_url_by_point(600,300)
           
        end
        my_loc.zoom_level = '16'
        @bio = get_artist_bio('')
    end

    private
    def search_id(results, id)
        results.each do |event|
            if(event.id ==  id.to_i)
                return event
            end
        end
        render_not_found
    end

    private
    def render_not_found
        render :file => "#{Rails.root}/public/404.html",  :status => 404
    end

    private
    def get_venue_by_id(id)
        remote = Songkickr::Remote.new ENV["SONGKICK_API_KEY"]
        @venue = remote.venue(id)
        return @venue
    end

    private
    def show_top_artists
        lastfm = Lastfm.new(ENV["LASTFM_API_KEY"], ENV["LASTFM_API_SECRET"])
        token = lastfm.auth.get_token
        return lastfm.chart.get_top_artists
    end

     private
     def get_artist_bio(artist)
         lastfm = Lastfm.new(ENV["LASTFM_API_KEY"], ENV["LASTFM_API_SECRET"])
         token = lastfm.auth.get_token
         lastfm.session = lastfm.auth.get_session(token: token)['key']

         return lastfm.artist.getInfo(artist: artist)
     end

    # Only allow a list of trusted parameters through.
    def concert_params
      params.require(:concert).permit(:name, :id, :venue)
    end
end
