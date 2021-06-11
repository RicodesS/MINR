class CallbacksController < Devise::OmniauthCallbacksController
  def twitter
    @user = User.from_ominauth(request.env["omniauth.auth"])
    signin_and_redirect @user
  end

  def ban
  	@user = User.find(params[:id])
end
