class ReportsController < ApplicationController
  before_action :authenticate_user!
  respond_to :js, :json, :html

  def new
  	super
  end

  def create
  		@rep = Report.new
		@rep.comment_id = params[:comment]
		@rep.user_id = current_user.id
		@rep.ut = params[:ut]
    @rep.verif = params[:verif]
    @rep.reason = params[:rea]
		@rep.save
		redirect_to artist_path(id: params[:artist]), :notice => "Reported."
  end
public
  def self.destroy_ut(id)
  	@reps = Report.all
  	@reps.each do |r|
  		if(r.ut.to_s == id.to_s)
  			r.destroy
  		end
  	end
  end
end
