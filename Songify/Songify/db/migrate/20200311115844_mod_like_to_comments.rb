class ModLikeToComments < ActiveRecord::Migration[6.0]
  def change
change_column :comments, :like, :integer, :default=>0
  end
end
