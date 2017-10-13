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
.controller('GlobalCtrl', [ '$rootScope', '$stateParams',
function($rootScope,$stateParams) {
  
}]);