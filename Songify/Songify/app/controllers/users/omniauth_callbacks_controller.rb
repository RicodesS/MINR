# frozen_string_literal: true

class Users::OmniauthCallbacksController < Devise::OmniauthCallbacksController
  # You should configure your model like this:
  # devise :omniauthable, omniauth_providers: [:twitter]

  # You should also create an action method in this controller like this:
  def twitter
    @user = User.create_from_provider_data(request.env['omniauth.auth'])
    if @user.persisted?
      sign_in_and_redirect @user
      set_flash_message(:notice, :success, kind: 'Twitter') if is_navigational_format?
    else
      flash[:error] = 'There was a problem signing you in through Twitter. Please register or try signing in later.'
      redirect_to new_user_registration_url
    end
  end

  # More info at:
  # https://github.com/plataformatec/devise#omniauth

  # GET|POST /resource/auth/twitter
  def passthru
    super
  end

=begin def after_sign_in_path_for(resource)
    if resource.email_verified?
      super resource
    else
      finish_signup_path(resource)
    end
  end
=end

  # GET|POST /users/auth/twitter/callback
  def failure
    flash[:error] = 'There was a problem signing you in. Please register or try signing in later.'
    redirect_to new_user_registration_url
  end

  # protected

  # The path used when OmniAuth fails
  def after_omniauth_failure_path_for(scope)
    super(scope)
  end
end
