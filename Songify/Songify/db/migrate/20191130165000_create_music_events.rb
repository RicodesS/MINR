class CreateMusicEvents < ActiveRecord::Migration[6.0]
  def change
    create_table :music_events do |t|
      t.string :title
      t.text :body

      t.timestamps
    end
  end
end
