class ModDislikeToComments < ActiveRecord::Migration[6.0]
  def change
  	change_column :comments, :dislike, :integer, :default=>0
  end
end
