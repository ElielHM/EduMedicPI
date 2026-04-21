  let navbarToggler = document.querySelector(".navbar-toggler");
  const navbarCollapse = document.querySelector(".navbar-collapse");


  document.querySelectorAll(".page-scroll").forEach((e) =>
    e.addEventListener("click", () => {
      navbarToggler.classList.remove("active");
      navbarCollapse.classList.remove("show");
    })
  );
  navbarToggler.addEventListener("click", function () {
    navbarToggler.classList.toggle("active");
  });
    /*=====================================
    Sticky
    ======================================= */
  window.onscroll = function () {
    const header_navbar = document.querySelector(".navbar-area");
    const sticky = header_navbar.offsetTop;
    const logo = document.querySelector(".navbar-brand img");


    if (window.pageYOffset > sticky) {
      header_navbar.classList.add("sticky");
      logo.src = "static/img/logo.svg";
    } else {
      header_navbar.classList.remove("sticky");
      logo.src = "static/img/logo.svg";
    }}



  // WOW active
  new WOW().init();