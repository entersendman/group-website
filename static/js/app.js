angular.module('overstudio', ['ui.router'])
.config(function($stateProvider,$urlRouterProvider) {
  var homeState = {
    name: 'home',
    url: '/',
    templateUrl: '/about.html',
    controller: 'MainCtrl'
  }

  var worksState = {
    name: 'work',
    url: '/works',
    templateUrl: '/works.html',
    controller: 'WorksCtrl'
  }

  var contactState = {
    name: 'contact',
    url: '/contact',
    templateUrl: '/contact.html',
    controller: 'ContactCtrl'
  }

  $stateProvider.state(homeState);
  $stateProvider.state(worksState);
  $stateProvider.state(contactState);
  $urlRouterProvider.otherwise('/');
})

.controller('MainCtrl', ['$scope', function($scope) {
     $scope.subscriberName ;
$scope.subscriberEmail ;
$scope.subscribe = function() {

$scope.data = {name:$scope.subscriberName, email: $scope.subscriberEmail};

$.ajax({
	url: "http://0.0.0.0:8000/cgi-bin/form.py",
	type: "post",
	datatype:"json",
	data: $scope.data,
	success: function(response){
	    alert(response.message);
	    alert(response.keys);
	}
});
}
}]);

