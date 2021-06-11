# frozen_string_literal: true

class Users::RegistrationsController < Devise::RegistrationsController
  before_action :configure_sign_up_params, only: [:create]

# /resource/sign_up
   def new
     super
    UserMailer.welcome_email(self).deliver_now
   end

  # POST /resource
   def create
    super
  end

  # GET /resource/edit
  def edit
     super
   end

  # PUT /resource
   def update
     self.resource = resource_class.to_adapter.get!(send(:"current_#{resource_name}").to_key)

   if resource.update_with_password(params[resource_name])
     set_flash_message :notice, :updated if is_navigational_format?
     sign_in resource_name, resource, :bypass => true
     respond_with resource, :location => after_update_path_for(resource)
   else
     clean_up_passwords(resource)
     respond_with_navigational(resource){ render_with_scope :edit }
   end
  end

  # DELETE /resource
   def destroy
     super
   end

  # GET /resource/cancel
  # Forces the session data which is usually expired after sign
  # in to be expired now. This is useful if the user wants to
  # cancel oauth signing in/up in the middle of the process,
  # removing all OAuth session data.
  def cancel
    super
  end

  # If you have extra params to permit, append them to the sanitizer.
  def configure_sign_up_params
     devise_parameter_sanitizer.permit(:sign_up, keys: [:attribute])
     devise_parameter_sanitizer.permit(:sign_up, keys: [:name])
  end

  # If you have extra params to permit, append them to the sanitizer.
 

  # The path used after sign up.
  def after_sign_up_path_for(resource)
     super(resource)
  end

  # The path used after sign up for inactive accounts.
  # def after_inactive_sign_up_path_for(resource)
  #   super(resource)
  # end

  private
  # Notice the name of the method
  def sign_up_params
    params.require(:user).permit(:name, :email, :gender, :location, :password, :password_confirmation)
  end
end
