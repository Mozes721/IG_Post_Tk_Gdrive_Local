Object.defineProperty(exports, '__esModule', {
  value: true
});

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var _os = require('os');

var _os2 = _interopRequireDefault(_os);

// Public: GrammarUtils.OperatingSystem - a module which exposes different
// platform related helper functions.
'use babel';

exports['default'] = {
  isDarwin: function isDarwin() {
    return this.platform() === 'darwin';
  },

  isWindows: function isWindows() {
    return this.platform() === 'win32';
  },

  isLinux: function isLinux() {
    return this.platform() === 'linux';
  },

  platform: function platform() {
    return _os2['default'].platform();
  },

  architecture: function architecture() {
    return _os2['default'].arch();
  },

  release: function release() {
    return _os2['default'].release();
  }
};
module.exports = exports['default'];
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL21vemVzNzIxLy5hdG9tL3BhY2thZ2VzL3NjcmlwdC9saWIvZ3JhbW1hci11dGlscy9vcGVyYXRpbmctc3lzdGVtLmpzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7Ozs7OztrQkFFZSxJQUFJOzs7Ozs7QUFGbkIsV0FBVyxDQUFDOztxQkFNRztBQUNiLFVBQVEsRUFBQSxvQkFBRztBQUNULFdBQU8sSUFBSSxDQUFDLFFBQVEsRUFBRSxLQUFLLFFBQVEsQ0FBQztHQUNyQzs7QUFFRCxXQUFTLEVBQUEscUJBQUc7QUFDVixXQUFPLElBQUksQ0FBQyxRQUFRLEVBQUUsS0FBSyxPQUFPLENBQUM7R0FDcEM7O0FBRUQsU0FBTyxFQUFBLG1CQUFHO0FBQ1IsV0FBTyxJQUFJLENBQUMsUUFBUSxFQUFFLEtBQUssT0FBTyxDQUFDO0dBQ3BDOztBQUVELFVBQVEsRUFBQSxvQkFBRztBQUNULFdBQU8sZ0JBQUcsUUFBUSxFQUFFLENBQUM7R0FDdEI7O0FBRUQsY0FBWSxFQUFBLHdCQUFHO0FBQ2IsV0FBTyxnQkFBRyxJQUFJLEVBQUUsQ0FBQztHQUNsQjs7QUFFRCxTQUFPLEVBQUEsbUJBQUc7QUFDUixXQUFPLGdCQUFHLE9BQU8sRUFBRSxDQUFDO0dBQ3JCO0NBQ0YiLCJmaWxlIjoiL2hvbWUvbW96ZXM3MjEvLmF0b20vcGFja2FnZXMvc2NyaXB0L2xpYi9ncmFtbWFyLXV0aWxzL29wZXJhdGluZy1zeXN0ZW0uanMiLCJzb3VyY2VzQ29udGVudCI6WyIndXNlIGJhYmVsJztcblxuaW1wb3J0IG9zIGZyb20gJ29zJztcblxuLy8gUHVibGljOiBHcmFtbWFyVXRpbHMuT3BlcmF0aW5nU3lzdGVtIC0gYSBtb2R1bGUgd2hpY2ggZXhwb3NlcyBkaWZmZXJlbnRcbi8vIHBsYXRmb3JtIHJlbGF0ZWQgaGVscGVyIGZ1bmN0aW9ucy5cbmV4cG9ydCBkZWZhdWx0IHtcbiAgaXNEYXJ3aW4oKSB7XG4gICAgcmV0dXJuIHRoaXMucGxhdGZvcm0oKSA9PT0gJ2Rhcndpbic7XG4gIH0sXG5cbiAgaXNXaW5kb3dzKCkge1xuICAgIHJldHVybiB0aGlzLnBsYXRmb3JtKCkgPT09ICd3aW4zMic7XG4gIH0sXG5cbiAgaXNMaW51eCgpIHtcbiAgICByZXR1cm4gdGhpcy5wbGF0Zm9ybSgpID09PSAnbGludXgnO1xuICB9LFxuXG4gIHBsYXRmb3JtKCkge1xuICAgIHJldHVybiBvcy5wbGF0Zm9ybSgpO1xuICB9LFxuXG4gIGFyY2hpdGVjdHVyZSgpIHtcbiAgICByZXR1cm4gb3MuYXJjaCgpO1xuICB9LFxuXG4gIHJlbGVhc2UoKSB7XG4gICAgcmV0dXJuIG9zLnJlbGVhc2UoKTtcbiAgfSxcbn07XG4iXX0=