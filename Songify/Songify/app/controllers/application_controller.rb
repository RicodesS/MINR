class ApplicationController < ActionController::Base
    protect_from_forgery with: :exception
    include SessionsHelper
    before_action :configure_permitted_parameters, if: :devise_controller?

  protected
  def configure_permitted_parameters
    devise_parameter_sanitizer.permit(:sign_up, keys: [:username, :date_of_birth, :gender, :location,
                                      :first_name, :last_name])
    devise_parameter_sanitizer.permit(:sign_in, keys: [:username])
    devise_parameter_sanitizer.permit(:account_update, keys: [:username, :date_of_birth, :gender,
                                      :first_name, :last_name, :twittername, :created_at,:location, :profile_picture_url, :avatar, :avatar_cache, :remove_avatar, :ban, :bio])
    
  end

  def favorite_text
    return @favorite_exists ? "UnFavorite" : "Favorite"
  end

  helper_method :favorite_text
end
