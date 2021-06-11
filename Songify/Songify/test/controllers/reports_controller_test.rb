require 'test_helper'

class ReportsControllerTest < ActionDispatch::IntegrationTest
  test "should get create" do
    get reports_create_url
    assert_response :success
  end

end
