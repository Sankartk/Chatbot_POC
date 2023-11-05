// app.js
angular.module('chatApp', [])
.controller('ChatController', function($scope, $http) {
  // Base URL for the FastAPI backend
  var baseUrl = 'http://localhost:8000'; // Update this if your backend URL is different

  $scope.chatMessages = [];
  $scope.newMessage = '';
  $scope.employees = []; // This will hold the list of employees
  $scope.departmentName = ''; // This will hold the department name entered by the user

  $scope.sendMessage = function() {
    const message = {
      user_message: $scope.newMessage
    };
    // Send the message to the backend
    $http.post(baseUrl + '/chat/', message).then(function(response) {
      // Push the sent message and the bot's response to the chatMessages array
      $scope.chatMessages.push({
        username: 'You',
        text: message.user_message
      }, {
        username: 'Bot',
        text: response.data.response
      });
      // Clear the input field
      $scope.newMessage = '';
    }, function(error) {
      console.error('Error sending message:', error);
    });
  };

  $scope.checkIfEnterKey = function(event) {
    if(event.keyCode === 13) { // Enter key code
      $scope.sendMessage();
    }
  };

  // Function to fetch chatlogs from the backend
  $scope.getChatlogs = function() {
    $http.get(baseUrl + '/chatlogs').then(function(response) {
      // Assuming the backend returns an array of chat logs
      $scope.chatMessages = response.data.map(function(log) {
        return {
          username: 'User',
          text: log.user_message || (log[Object.keys(log)[0]]).user_message
        };
      });
    }, function(error) {
      console.error('Error fetching chatlogs:', error);
    });
  };

  $scope.getEmployeesByDepartment = function(department) {
    $http.get(baseUrl + '/employees/', { params: { department: department } })
      .then(function(response) {
        // Transform the response to an array of employee objects
        var employees = [];
        angular.forEach(response.data, function(employeeData) {
          angular.forEach(employeeData, function(employee) {
            employees.push(employee);
          });
        });
        $scope.employees = employees;
      }, function(error) {
        console.error('Error getting employees:', error);
      });
  };
    
  // Fetch chatlogs on controller initialization
  $scope.getChatlogs();
});
