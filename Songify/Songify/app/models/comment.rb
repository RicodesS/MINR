class Comment < ApplicationRecord
  has_many :reports, dependent: :destroy
  belongs_to :user
  acts_as_votable
end

