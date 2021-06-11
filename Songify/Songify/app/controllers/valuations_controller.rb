class ValuationsController < ApplicationController
	 respond_to :js, :json, :html

	def new
		super	  
	end

	def index
		@val = Valuation.all
	end

	def create
		@val = Valuation.new
		@val.artist = params[:artist]
		@val.user = current_user
		@val.value = params[:value]
		@val.save
		redirect_to artist_path(id: params[:artist]), :notice => "Reviewed."
	end


    def update
    @val = Valuation.find(params[:valuation_id])
 if @val.update_attribute(:value, params[:value])
  redirect_to artist_path(@val.artist), :notice => "Valuation updated."
 else
  redirect_to artist_path(@val.artist), :alert => "Unable to update valuation."
 end
end

	def destroy
    @val = Valuation.find(params[:id])
    @artist = @val.artist 
    @val.destroy
  	redirect_to artist_path(id: @artist), :notice => "Comment removed."
  end
end
