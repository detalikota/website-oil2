function myFunction() {
    document.getElementById("myDropdown").classList.toggle("bottom-dropdown-show");
  }
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("bottom-dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('bottom-dropdown-show')) {
          openDropdown.classList.remove('bottom-dropdown-show');
        }
      }
    }
  }