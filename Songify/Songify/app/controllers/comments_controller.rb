class CommentsController < ApplicationController
 before_action :authenticate_user!
 respond_to :js, :json, :html

  def new
  	super
  end

  def create
  	@comment = Comment.new
  	@comment.artist = params[:artist]
  	@comment.user = current_user
  	@comment.body = params[:body]
  	@comment.save
  	redirect_to artist_path(id: params[:artist]), :notice => "Commented."
  end

    def update
    @comment = Comment.find(params[:id])
 if @comment.update_attributes(body: params[:body])
  redirect_to artist_path(@comment.artist), :notice => "Comment updated."
 else
  redirect_to artist_path(@comment.artist), :alert => "Unable to update comment."
 end
end

  def show 
  	@comments =Comment.all
  end

  def like
  	@comment = Comment.find(params[:id])
  	if !current_user.liked? @comment
  		@comment.liked_by current_user
  	elsif current_user.liked? @comment
  		@comment.unliked_by current_user
  	end
  	redirect_to artist_path(@comment.artist)
  end
  def dislike
  	@comment = Comment.find(params[:id])
  	if !current_user.disliked? @comment
  		@comment.disliked_by current_user
  	elsif current_user.disliked? @comment
  		@comment.undisliked_by current_user
  	end
    redirect_to artist_path(@comment.artist)
  end

  

  def destroy
    @comment = Comment.find(params[:id])
    @artist = @comment.artist 
    @comment.destroy
  	redirect_to artist_path(id: @artist), :notice => "Comment removed."
  end

  private
  def comment_params
  	params.require(:comment).permit(:body, :artist, :user_id, :like, :dislike)
  end
end
