require 'test_helper'

class ValuationsControllerTest < ActionDispatch::IntegrationTest
  test "should get create" do
    get valuations_create_url
    assert_response :success
  end

end
