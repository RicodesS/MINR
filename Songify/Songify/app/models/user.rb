class User < ApplicationRecord
  mount_uploader :avatar, AvatarUploader
  has_many :comments, dependent: :destroy
  has_many :reports, dependent: :destroy
  has_many :valuations, dependent: :destroy
  acts_as_voter
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable,
         :confirmable, :lockable, :timeoutable,
         :omniauthable, omniauth_providers: [:twitter]

  #attr_accessor :email, :password, :remember_me, :avatar, :avatar_cache, :remove_avatar

#  enum gender: {undisclosed: 0, female:1, male:2, other:3}
  validates_presence_of   :username
  validates_integrity_of  :avatar
  validates_processing_of :avatar
  def profile_image_uri(size = :mini)
  parse_encoded_uri(insecure_uri(profile_image_uri_https(size))) unless @attrs[:profile_image_url_https].nil?
  end

  def self.create_from_provider_data(auth)
    where(provider: auth.provider, uid: auth.uid).first_or_create do |user|
      user.username = auth.info.nickname
      user.first_name  = auth.info.name              # assuming the user model has a name
      user.email = auth.info.email            # since we are using twitter, which hasn't got any email, we'll just comment this
      user.password = 123456
      user.provider = auth.provider
      user.profile_image_url = auth[:extra][:raw_info][:profile_image_url]
      # If you are using confirmable and the provider(s) you use validate emails,
      # uncomment the line below to skip the confirmation emails.
      user.skip_confirmation!
    end
  end

  after_create :welcome_send
  def welcome_send
    UserMailer.welcome_email(self).deliver_now
    #redirect_to concerts_path, alert: "Thank you."
  end

  def email_required?
    super && provider.blank?
  end

  def active_for_authentication? 
    super && !ban? 
  end 
  
  def inactive_message 
    !ban? ? super : :not_ban
  end
end
