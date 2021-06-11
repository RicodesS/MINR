class AddLikeToComments < ActiveRecord::Migration[6.0]
  def change
    add_column :comments, :like, :integer
  end
end
