class CreateReports < ActiveRecord::Migration[6.0]
  def change
    create_table :reports do |t|
      t.string :comment
      t.string :user
      t.string :reason
      t.references :user, null: false, foreign_key: true

      t.timestamps
    end
  end
end
