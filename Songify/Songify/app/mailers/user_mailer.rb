class UserMailer < ApplicationMailer
	 default from: 'songify@info.com'
 
  def welcome_email(user)
    @user = user
    @url  = 'http://example.com/login'
    mail(to: @user.email, subject: 'Confirm your e-mail')
  end

  def confirmation_instructions(record, token, opts={})
    welcome_email(record)
  end

end
