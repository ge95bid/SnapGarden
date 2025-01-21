/**
 * WEBSITE: https://themefisher.com
 * TWITTER: https://twitter.com/themefisher
 * FACEBOOK: https://www.facebook.com/themefisher
 * GITHUB: https://github.com/themefisher/
 */

/*=== MEDIA QUERY ===*/
@import url("https://fonts.googleapis.com/css?family=Lora:400,400i|Open+Sans:300,400,600,700,800");
body {
  font-family: "Open Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4, h5, h6 {
  font-family: "Open Sans", sans-serif;
  color: #000;
  font-weight: 300;
}

h1 {
  font-size: 45px;
  line-height: 61px;
}

h2 {
  font-size: 40px;
  line-height: 50px;
}

h3 {
  font-size: 20px;
  line-height: 30px;
}

p, li, blockquote, label {
  font-size: 16px;
  letter-spacing: 0;
  line-height: 25px;
  color: #808080;
  margin-bottom: 0;
}

cite {
  font-size: 14px;
  font-style: normal;
}

.lora {
  font-family: "Lora", serif;
  font-style: italic;
}

.form-control::-webkit-input-placeholder {
  color: #808080;
  line-height: 25px;
  font-size: 16px;
}

ul.app-badge {
  margin-bottom: 60px;
}
ul.app-badge li a img {
  width: 150px;
  height: auto;
}
@media (max-width: 400px) {
  ul.app-badge li {
    margin-bottom: 10px;
  }
}

ul.post-tag {
  margin-bottom: 20px;
}
ul.post-tag li {
  font-size: 14px;
}
ul.post-tag li img {
  width: 25px;
  height: 25px;
  border-radius: 100%;
  margin-right: 5px;
}
ul.post-tag li a {
  font-size: 14px;
}
ul.post-tag li:last-child {
  margin-left: 25px;
}

ul.social-links {
  margin-bottom: 0;
}
ul.social-links li:first-child a {
  padding-left: 0;
}
ul.social-links li a {
  padding: 0 15px;
  display: block;
}
ul.social-links li a i {
  font-size: 20px;
  color: #000;
}

body {
  overflow-x: hidden;
}

.shadow, .coming-soon .block .count-down .syotimer-cell, .user-login .block .image img, .privacy .block, .job-list .block, .team-sm .image img, .founder img, .service .service-box {
  box-shadow: 0 7px 20px 0 rgba(0, 0, 0, 0.08);
}

.overlay:before {
  content: "";
  background: rgba(105, 140, 230, 0.1);
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

a {
  font-size: inherit;
  color: inherit;
}

a:focus,
a:hover {
  color: #2e7eed;
  text-decoration: none;
}

.bg-gray {
  background: #fafafa;
}

.bg-blue {
  background: #2e7eed;
}

.bg-1 {
  background: url(../images/background/promo-video-back.jpg) fixed no-repeat;
  background-size: cover;
}

.bg-coming-soon {
  background: url(../images/background/comming-soon.jpg) fixed no-repeat;
  background-size: cover;
  background-position: bottom;
}

.section {
  padding: 100px 0;
}

.section-title {
  text-align: center;
  margin-bottom: 80px;
}
.section-title h2 {
  font-size: 35px;
  margin-bottom: 13px;
}
.section-title p {
  width: 50%;
  margin: 0 auto;
}
@media (max-width: 480px) {
  .section-title p {
    width: 100%;
  }
}

.page-title {
  text-align: center;
}

.video {
  position: relative;
}
.video:before {
  border-radius: 3px;
}
.video img {
  width: 100%;
  border-radius: 8px;
}
.video .video-button {
  position: absolute;
  left: 0;
  top: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}
.video .video-box a {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.video .video-box a i {
  height: 125px;
  width: 125px;
  font-size: 40px;
  background: #2e7eed;
  border-radius: 100%;
  color: #fff;
  line-height: 125px;
  text-align: center;
}
@media (max-width: 992px) {
  .video .video-box a i {
    height: 80px;
    width: 80px;
    line-height: 80px;
    font-size: 22px;
  }
}
.video .video-box a iframe {
  width: 100%;
  height: 100%;
}

.form-control.main {
  background: #fff;
  padding: 15px 20px;
  height: 48px;
  margin-bottom: 20px;
  border: 1px solid #cccccc;
  font-size: 14px;
}
.form-control.main:focus {
  border: 1px solid #2e7eed;
  box-shadow: none;
}

textarea.form-control.main {
  height: initial;
}

.form-control::-webkit-input-placeholder {
  color: #808080;
  font-size: 14px;
}

.left {
  overflow: hidden;
}
.left img {
  margin-left: -40px;
}
@media (max-width: 768px) {
  .left img {
    margin-left: 0;
    margin-bottom: 30px;
  }
}

.right {
  overflow: hidden;
}
.right img {
  margin-left: 40px;
}
@media (max-width: 768px) {
  .right img {
    margin-left: 0;
  }
}

.hide-overflow, .service {
  overflow: hidden;
}

.nav-up {
  top: -70px;
}

button:focus,
.slick-slide:focus {
  outline: 0;
}

.btn {
  text-transform: uppercase;
}

.btn-download {
  padding: 20px 35px;
  font-size: 14px;
  background: #fff;
  color: #2e7eed;
}
.btn-download span {
  margin-left: 5px;
  font-size: 20px;
}

.btn-main {
  padding: 25px 45px;
  border-radius: 3px;
  background: #2e7eed;
  color: #fff;
  outline: none;
}
.btn-main:hover {
  color: #fff;
}
.btn-main:focus {
  color: #fff;
  box-shadow: none;
}

.btn-main-md {
  padding: 17px 38px;
  border-radius: 3px;
  background: #2e7eed;
  color: #fff;
  outline: none;
}
.btn-main-md:hover {
  color: #fff;
}
.btn-main-md:focus {
  color: #fff;
  box-shadow: none;
}

.btn-main-sm {
  padding: 15px 35px;
  border-radius: 3px;
  background: #2e7eed;
  color: #fff;
  outline: none;
  font-size: 14px;
}
.btn-main-sm:hover {
  color: #fff;
}
.btn-main-sm:focus {
  color: #fff;
  box-shadow: none;
}

.btn-white {
  background: white;
  color: #2e7eed;
}

.btn-rounded-icon {
  border-radius: 100px;
  color: #fff;
  border: 1px solid #fff;
  padding: 13px 50px;
}

.main-nav {
  background: #fff;
  z-index: 1;
}
.main-nav .navbar-brand {
  padding: 0;
}
.main-nav .navbar-nav .nav-item {
  position: relative;
  font-family: "Open Sans", sans-serif;
}
.main-nav .navbar-nav .nav-item .nav-link {
  position: relative;
  text-align: center;
  font-size: 13px;
  text-transform: uppercase;
  font-weight: 600;
  color: #000;
  padding-left: 20px;
  padding-right: 20px;
  line-height: 45px;
}
@media (max-width: 992px) {
  .main-nav .navbar-nav .nav-item .nav-link {
    line-height: 25px;
  }
}
.main-nav .navbar-nav .nav-item .nav-link span i {
  font-size: 11px;
}
.main-nav .navbar-nav .nav-item.active .nav-link {
  color: #2e7eed;
}
.main-nav .navbar-nav .nav-item.active .nav-link:before {
  content: "";
  background: #2e7eed;
  width: 60%;
  height: 2px;
  position: absolute;
  top: 0;
  left: 20%;
}
@media (max-width: 992px) {
  .main-nav .navbar-nav .nav-item.active .nav-link:before {
    display: none;
  }
}
.main-nav .dropdown {
  position: relative;
}
.main-nav .dropdown .open > a,
.main-nav .dropdown .open > a:focus,
.main-nav .dropdown .open > a:hover {
  background: transparent;
}
.main-nav .dropdown.full-width .dropdown-menu {
  left: 0 !important;
  right: 0 !important;
}
@media (max-width: 992px) {
  .main-nav .dropdown {
    transform: none;
    left: auto;
    position: relative;
    text-align: center;
  }
}
.main-nav .dropdown .dropdown-menu {
  border-radius: 0;
  padding: 0;
  border: 0;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
  display: none;
  margin-top: 0;
}
.main-nav .dropdown .dropdown-menu.show {
  display: block;
}
@media (max-width: 992px) {
  .main-nav .dropdown .dropdown-menu {
    text-align: center;
    float: left !important;
    width: 100%;
    margin: 0;
  }
}
.main-nav .dropdown .dropdown-menu .dropdown-item {
  font-size: 13px;
  padding: 3px 22px;
  transition: 0.3s ease;
}
.main-nav .dropdown .dropdown-menu .dropdown-item.active, .main-nav .dropdown .dropdown-menu .dropdown-item.focus, .main-nav .dropdown .dropdown-menu .dropdown-item:focus, .main-nav .dropdown .dropdown-menu .dropdown-item:hover {
  background-color: transparent;
  color: #2e7eed;
}
.main-nav .dropdown .dropdown-menu li:first-child {
  margin-top: 10px;
}
.main-nav .dropdown .dropdown-menu li:last-child {
  margin-bottom: 10px;
}
@media (min-width: 992px) {
  .main-nav .dropdown .dropdown-menu {
    position: absolute;
    display: block;
    visibility: hidden;
    opacity: 0;
    transform: translateY(10px);
    transition: visibility 0.2s, opacity 0.2s, transform 500ms cubic-bezier(0.43, 0.26, 0.11, 0.99);
  }
  .main-nav .dropdown:hover > .dropdown-menu {
    opacity: 1;
    visibility: visible;
    color: #777;
    transform: translateY(0px);
  }
}

.dropdown-submenu.active > a,
.dropdown-submenu:hover > a {
  color: #2e7eed;
}

.dropleft .dropdown-menu,
.dropright .dropdown-menu {
  margin: 0;
}

.dropdown-toggle::after {
  display: none;
}

.dropleft .dropdown-toggle::before,
.dropright .dropdown-toggle::after {
  font-weight: bold;
  font-family: "themify";
  border: 0;
  font-size: 8px;
  vertical-align: 1px;
}

.dropleft .dropdown-toggle::before {
  content: "\e64a";
  margin-right: 5px;
}

.dropright .dropdown-toggle::after {
  content: "\e649";
  margin-left: 5px;
}

.navbar-toggler:focus,
.navbar-toggler:hover {
  outline: none;
}

.footer-main {
  padding: 92px 0;
  background: #1a1b1f;
}
@media (max-width: 768px) {
  .footer-main {
    padding: 50px 0;
  }
}
.footer-main .block img {
  margin-bottom: 20px;
}
.footer-main .block img #small-Apps {
  fill: red;
}
.footer-main .block ul.social-icon li a {
  text-decoration: none;
  display: block;
  width: 38px;
  height: 38px;
  border-radius: 100%;
  background: #3f3f43;
  color: #fff;
  text-align: center;
  line-height: 38px;
}
@media (max-width: 768px) {
  .footer-main .block {
    margin-bottom: 40px;
  }
}
.footer-main .block-2 h6 {
  font-weight: bold;
  font-size: 14px;
  text-transform: uppercase;
  color: #fff;
  margin-bottom: 25px;
}
.footer-main .block-2 ul {
  padding: 0;
}
.footer-main .block-2 ul li {
  margin-bottom: 10px;
  list-style: none;
}
.footer-main .block-2 ul li a {
  font-size: 14px;
  color: #6f6f71;
  transition: 0.2s ease;
}
.footer-main .block-2 ul li a:hover {
  color: #fff;
}

.footer-classic {
  background: #fafafa;
  text-align: center;
  padding: 110px 0;
}
.footer-classic ul.social-icons {
  margin-bottom: 30px;
}
@media (max-width: 480px) {
  .footer-classic ul.social-icons li {
    margin-bottom: 10px;
  }
}
.footer-classic ul.social-icons li a {
  padding: 0 20px;
  display: block;
}
.footer-classic ul.social-icons li a i {
  font-size: 25px;
  color: #000;
}
.footer-classic ul.footer-links li a {
  padding: 0 10px;
  display: block;
  font-weight: bold;
  text-transform: uppercase;
  font-size: 14px;
  color: #000;
}

.scroll-top-to {
  position: fixed;
  right: 20px;
  bottom: 50px;
  width: 40px;
  height: 40px;
  line-height: 40px;
  text-align: center;
  background: #2e7eed;
  color: #fff;
  transition: 0.3s;
  z-index: 999556;
  cursor: pointer;
  display: none;
}
.scroll-top-to:hover {
  background: #333;
}
@media (max-width: 768px) {
  .scroll-top-to {
    bottom: 15px;
    right: 15px;
    width: 35px;
    height: 35px;
    line-height: 35px;
  }
}

.call-to-action-app {
  text-align: center;
}
.call-to-action-app h2,
.call-to-action-app p,
.call-to-action-app a {
  color: #fff !important;
}
.call-to-action-app p {
  margin-bottom: 60px;
}
.call-to-action-app ul li {
  margin: 10px;
}
@media (max-width: 480px) {
  .call-to-action-app ul li {
    margin-left: 0;
    margin-bottom: 10px;
  }
}
.call-to-action-app ul li:first-child {
  margin-left: 0;
}
.call-to-action-app ul li a i {
  font-size: 20px;
  margin-right: 5px;
}

.cta-hire {
  background: #FAFAFA;
}
.cta-hire p {
  width: 65%;
  margin: 0 auto;
}
.cta-hire h2,
.cta-hire p {
  margin-bottom: 20px;
}

.cta-community {
  margin-bottom: 50px;
  padding: 40px 100px;
}
@media (max-width: 992px) {
  .cta-community {
    padding: 40px;
  }
}

.jd-modal .modal-content {
  padding: 25px;
  text-align: left;
  background: #fafafa;
}
.jd-modal .modal-content .modal-header .modal-title {
  color: #000;
}
.jd-modal .modal-content .modal-body .block-2 {
  display: flex;
  margin-bottom: 70px;
}
.jd-modal .modal-content .modal-body .block-2 .title {
  width: 30%;
}
.jd-modal .modal-content .modal-body .block-2 .title p {
  color: #000;
}
.jd-modal .modal-content .modal-body .block-2 .details {
  width: 70%;
}
.jd-modal .modal-content .modal-body .block-2 .details ul {
  padding-left: 0;
  margin: 0;
}
.jd-modal .modal-content .modal-body .block-2 .details ul li {
  list-style: none;
  margin-bottom: 5px;
}
.jd-modal .modal-content .modal-body .block-2 .details ul li span {
  padding-right: 5px;
  color: #000;
}
.jd-modal .modal-content .modal-body .form-title {
  margin-bottom: 30px;
}

.banner {
  padding: 100px 0;
}
.banner .block h1 {
  margin-bottom: 13px;
}
.banner .block p {
  font-size: 20px;
  margin-bottom: 30px;
}
.banner .block .video {
  width: 80%;
  margin: 0 auto;
}
@media (max-width: 768px) {
  .banner .block .video {
    width: 100%;
  }
}
.banner .block ul.clients-logo {
  margin-top: 30px;
}
.banner .block ul.clients-logo li {
  margin-left: 30px;
}
@media (max-width: 480px) {
  .banner .block ul.clients-logo li {
    margin-bottom: 20px;
  }
}
.banner .block ul.clients-logo li:first-child {
  margin-left: 0;
}

.slider {
  padding: 180px 0 300px;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.slider .block {
  position: relative;
}
.slider .block h1,
.slider .block h3 {
  color: #fff;
}
.slider .block .download {
  margin-top: 20px;
}
.slider .block .image-content {
  text-align: center;
}
.slider .block .image-content img {
  margin-top: 100px;
  margin-bottom: -200px;
}
.slider:before {
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  border-bottom: 290px solid #fff;
  border-left: 2000px solid transparent;
  width: 0;
}

.services .service-block {
  background: #fff;
  padding: 30px 40px;
  margin-bottom: 30px;
  border-radius: 5px;
}
.services .service-block:last-child {
  margin-bottom: 0;
}
@media (max-width: 480px) {
  .services .service-block:last-child {
    margin-bottom: 30px;
  }
}
.services .service-block h3 {
  line-height: 30px;
  text-transform: capitalize;
  font-size: 16px;
  font-weight: 500;
}
.services .service-block i {
  font-size: 30px;
  color: #2e7eed;
  margin-bottom: 15px;
  display: inline-block;
}
.services .service-block p {
  margin-bottom: 0;
  font-size: 14px;
  line-height: 20px;
}
.services .app-preview {
  display: flex;
  justify-content: center !important;
}
.services .app-preview img {
  height: 500px;
  width: auto;
}
@media (max-width: 992px) {
  .services .col-lg-4.m-auto {
    display: none;
  }
}

@media (max-width: 768px) {
  .service .service-thumb {
    width: 80%;
    margin: 0 auto;
  }
}
.service .service-box {
  padding: 20px;
  background: #fff;
  border-radius: 4px;
}
@media (max-width: 768px) {
  .service .service-box {
    width: 80%;
    margin: 0 auto;
  }
}
.service .service-box .service-item {
  text-align: center;
  padding: 10px;
  margin: 20px 0;
}
.service .service-box .service-item i {
  font-size: 20px;
  color: #2e7eed;
  display: inline-block;
  margin-bottom: 10px;
}
.service .service-box .service-item p {
  font-size: 14px;
}

.feature .feature-content h2,
.feature .feature-content p {
  margin-bottom: 25px;
}
@media (max-width: 768px) {
  .feature .feature-content h2,
.feature .feature-content p {
    text-align: center;
  }
}
@media (max-width: 768px) {
  .feature .testimonial {
    text-align: center;
  }
}
.feature .testimonial p {
  font-family: "Lora", serif;
  margin-bottom: 10px;
  font-style: italic;
  color: #242424;
}
.feature .testimonial ul.meta li {
  font-size: 12px;
  margin-right: 10px;
}
.feature .testimonial ul.meta li img {
  height: 40px;
  width: 40px;
  border-radius: 100%;
}

@media (max-width: 480px) {
  .app-features .app-feature {
    margin-bottom: 30px;
  }
}
.app-features .app-explore {
  display: flex;
  justify-content: center !important;
  margin-bottom: 40px;
}

.banner-full .image {
  display: flex;
  justify-content: center;
}
.banner-full .image img {
  height: 625px;
}
@media (max-width: 768px) {
  .banner-full .image {
    margin-bottom: 30px;
  }
}
@media (max-width: 768px) {
  .banner-full .block {
    text-align: center;
  }
}
.banner-full .block .logo {
  margin-bottom: 40px;
}
.banner-full .block h1 {
  margin-bottom: 40px;
}
.banner-full .block p {
  font-size: 20px;
  margin-bottom: 50px;
}
.banner-full .block .app {
  margin-bottom: 20px;
}

.video-promo {
  padding: 150px 0;
}
.video-promo .content-block {
  width: 60%;
  margin: 0 auto;
  text-align: center;
}
.video-promo .content-block h2 {
  font-size: 30px;
  color: #fff;
}
.video-promo .content-block p {
  margin-bottom: 30px;
}
.video-promo .content-block a i.video {
  height: 125px;
  width: 125px;
  background: #2e7eed;
  display: inline-block;
  font-size: 40px;
  color: #fff;
  text-align: center;
  line-height: 125px;
  border-radius: 100%;
}
.video-promo .content-block a:focus {
  outline: 0;
}

.testimonial .testimonial-slider .item {
  padding-bottom: 10px;
}
.testimonial .testimonial-slider .item .block {
  padding: 40px;
  text-align: center;
  margin: 10px;
  border-radius: 5px;
}
.testimonial .testimonial-slider .item .block .image {
  margin-top: 30px;
  margin-bottom: 5px;
  width: 100%;
  display: flex;
  justify-content: center;
}
@media (max-width: 768px) {
  .testimonial .testimonial-slider .item .block .image {
    flex-grow: 1;
  }
}
.testimonial .testimonial-slider .item .block .image img {
  height: 40px;
  width: 40px;
  border-radius: 100%;
}
.testimonial .testimonial-slider .item .block p {
  font-family: "Lora", serif;
  font-style: italic;
  color: #888888;
}
.testimonial .testimonial-slider .item .block cite {
  font-style: normal;
  font-size: 14px;
  color: #161616;
}
.testimonial .testimonial-slider .owl-dots .owl-dot:hover span {
  background: #2e7eed;
}
.testimonial .testimonial-slider .owl-dots .owl-dot.active span {
  background: #2e7eed;
}

/* homepage 3 */
.gradient-banner {
  padding: 100px 0 170px;
  position: relative;
  overflow: hidden;
}
.gradient-banner::before {
  position: absolute;
  content: "";
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 200%;
  height: 200%;
  border-radius: 50%;
  background-image: linear-gradient(45deg, #009EC5 0%, #2e7eed 20%, #02225B 50%);
}

.pull-top {
  margin-top: -100px;
}

.shapes-container {
  position: absolute;
  overflow: hidden;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}
.shapes-container .shape {
  position: absolute;
}
.shapes-container .shape::before {
  content: "";
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(255, 255, 255, 0.1);
  transform: rotate(-35deg);
  position: absolute;
  border-radius: 50px;
}
.shapes-container .shape:nth-child(1) {
  top: 2%;
  left: 11%;
  width: 400px;
  height: 70px;
}
.shapes-container .shape:nth-child(2) {
  top: 14%;
  left: 18%;
  width: 200px;
  height: 15px;
}
.shapes-container .shape:nth-child(3) {
  top: 80%;
  left: 4%;
  width: 300px;
  height: 60px;
}
.shapes-container .shape:nth-child(4) {
  top: 85%;
  left: 15%;
  width: 100px;
  height: 10px;
}
.shapes-container .shape:nth-child(5) {
  top: 5%;
  left: 50%;
  width: 300px;
  height: 25px;
}
.shapes-container .shape:nth-child(6) {
  top: 4%;
  left: 52%;
  width: 200px;
  height: 5px;
}
.shapes-container .shape:nth-child(7) {
  top: 80%;
  left: 70%;
  width: 200px;
  height: 5px;
}
.shapes-container .shape:nth-child(8) {
  top: 55%;
  left: 95%;
  width: 200px;
  height: 5px;
}
.shapes-container .shape:nth-child(9) {
  top: 50%;
  left: 90%;
  width: 300px;
  height: 50px;
}
.shapes-container .shape:nth-child(10) {
  top: 30%;
  left: 60%;
  width: 500px;
  height: 55px;
}
.shapes-container .shape:nth-child(11) {
  top: 60%;
  left: 60%;
  width: 200px;
  height: 5px;
}
.shapes-container .shape:nth-child(12) {
  top: 35%;
  left: 75%;
  width: 200px;
  height: 5px;
}
.shapes-container .shape:nth-child(13) {
  top: 90%;
  left: 40%;
  width: 300px;
  height: 45px;
}
.shapes-container .shape:nth-child(14) {
  top: 54%;
  left: 75%;
  width: 200px;
  height: 5px;
}
.shapes-container .shape:nth-child(15) {
  top: 50%;
  left: 90%;
  width: 200px;
  height: 5px;
}
.shapes-container .shape:nth-child(16) {
  top: 50%;
  left: 81%;
  width: 100px;
  height: 5px;
}

.zindex-1 {
  z-index: 1;
}

hr {
  display: block;
  height: 2px;
  border: 0;
  border-top: 2px solid #2e7eed;
  margin: 1em 0;
  padding: 0;
}

.icon-box {
  height: 80px;
  width: 80px;
  text-align: center;
  background: #2e7eed;
}
.icon-box i {
  line-height: 80px;
  font-size: 30px;
}

.founder {
  margin-bottom: 30px;
}
.founder img {
  border-radius: 5px;
  margin-bottom: 25px;
}
.founder h2 {
  font-size: 30px;
  line-height: 30px;
}
.founder cite {
  font-size: 14px;
  font-style: normal;
}
.founder p {
  margin-top: 10px;
  font-size: 14px;
  margin-bottom: 20px;
}

.team-sm {
  margin-bottom: 30px;
}
.team-sm .image {
  position: relative;
  overflow: hidden;
  margin-bottom: 30px;
}
.team-sm .image img {
  border-radius: 5px;
}
.team-sm .image .social-links {
  position: absolute;
  background: #2e7eed;
  left: 0;
  right: 0;
  text-align: center;
  width: calc(100% - 80px);
  margin: 0 40px;
  border-radius: 4px;
  opacity: 0;
  transform: translate3d(0, 10px, 0);
  transition: 0.3s;
  bottom: 20px;
}
.team-sm .image .social-links ul {
  margin-bottom: 0;
}
.team-sm .image .social-links ul li a {
  display: block;
  padding: 15px;
}
.team-sm .image .social-links ul li a i {
  font-size: 20px;
  color: #fff;
}
.team-sm .image:hover .social-links {
  opacity: 1;
  transform: translate3d(0, 0, 0);
}
.team-sm h3 {
  margin-bottom: 0;
}
.team-sm cite {
  font-size: 14px;
  font-style: normal;
}
.team-sm p {
  margin-top: 15px;
}

.featured-article {
  padding: 0 0 50px 0;
}
.featured-article article.featured {
  display: flex;
}
@media (max-width: 768px) {
  .featured-article article.featured {
    flex-wrap: wrap;
  }
}
.featured-article article.featured .image {
  flex-basis: 100%;
  padding: 20px;
}
.featured-article article.featured .image img {
  width: 100%;
  border-radius: 8px;
}
@media (max-width: 768px) {
  .featured-article article.featured .image {
    margin-bottom: 20px;
  }
}
.featured-article article.featured .content {
  margin-left: 30px;
  flex-basis: 100%;
  align-self: center;
}
@media (max-width: 768px) {
  .featured-article article.featured .content {
    text-align: center;
  }
}
.featured-article article.featured .content h2 {
  margin-bottom: 20px;
}
.featured-article article.featured .content h2 a {
  font-size: 30px;
  color: #000;
  display: inline-block;
}
.featured-article article.featured .content h2 a:hover {
  color: #2e7eed;
}
.featured-article article.featured .content p {
  margin-bottom: 25px;
}

.post-sm {
  margin-bottom: 40px;
}
.post-sm .post-thumb {
  margin-bottom: 15px;
  overflow: hidden;
}
.post-sm .post-thumb img {
  transition: 0.3s ease;
}
.post-sm .post-title {
  margin-bottom: 15px;
}
.post-sm .post-title h3 a {
  color: #000;
  font-size: 20px;
}
.post-sm .post-title h3 a:hover {
  color: #2e7eed;
}
.post-sm:hover .post-thumb img {
  transform: scale(1.3);
}

.blog-single .single-post {
  padding-bottom: 70px;
}
.blog-single .single-post .post-body .feature-image {
  margin-bottom: 30px;
}
.blog-single .single-post .post-body .feature-image img {
  width: 100%;
}
.blog-single .single-post .post-body p {
  margin-bottom: 20px;
}
.blog-single .single-post .post-body .quote {
  padding: 30px 0;
  width: 80%;
  margin: 0 auto;
}
@media (max-width: 768px) {
  .blog-single .single-post .post-body .quote {
    width: 80%;
  }
}
.blog-single .single-post .post-body .quote blockquote {
  color: #000;
  padding: 10px 0 10px 30px;
  text-align: left;
  font-size: 30px;
  line-height: 40px;
  border-left: 6px solid #666666;
}
.blog-single .single-post .post-body .post-image {
  width: 60%;
  margin: 0 auto;
  margin-bottom: 20px;
}
.blog-single .about-author h2 {
  padding-bottom: 15px;
  border-bottom: 1px solid #cccccc;
  margin-bottom: 30px;
  font-size: 30px;
}
@media (max-width: 480px) {
  .blog-single .about-author h2 {
    text-align: center;
  }
}
@media (max-width: 480px) {
  .blog-single .about-author .media {
    flex-wrap: wrap;
  }
}
@media (max-width: 480px) {
  .blog-single .about-author .media .image {
    flex-grow: 1;
    width: 100%;
    display: flex;
    justify-content: center;
  }
}
.blog-single .about-author .media .image img {
  width: 150px;
  height: 150px;
  border-radius: 100%;
}
.blog-single .about-author .media .media-body {
  margin-left: 40px;
}
@media (max-width: 480px) {
  .blog-single .about-author .media .media-body {
    flex-grow: 1;
    width: 100%;
    text-align: center;
    margin-left: 0;
    margin-top: 20px;
  }
}
.blog-single .about-author .media .media-body p {
  margin-bottom: 15px;
}

.related-articles .title {
  margin-bottom: 20px;
}
.related-articles .title h2 {
  font-size: 30px;
}

.pagination-nav {
  display: flex;
  justify-content: center;
}
.pagination-nav ul.pagination {
  padding-top: 30px;
}
.pagination-nav ul.pagination li {
  margin-right: 10px;
}
.pagination-nav ul.pagination li a {
  border-radius: 3px;
  padding: 0;
  height: 50px;
  width: 50px;
  line-height: 50px;
  text-align: center;
  border-color: transparent;
  box-shadow: 0px 1px 3px 0px rgba(0, 0, 0, 0.1);
  color: #808080;
  transition: 0.3s ease-in;
}
.pagination-nav ul.pagination li a:hover {
  background-color: #2e7eed;
  color: #fff;
  border-color: transparent;
}
.pagination-nav ul.pagination .active a {
  background-color: #2e7eed;
  color: #fff;
  border-color: transparent;
}

@media (max-width: 480px) {
  .about .content {
    text-align: center;
  }
}
.about .content h2 {
  margin-bottom: 20px;
  text-transform: capitalize;
}
.about .about-slider .item {
  padding: 20px;
}
.about .about-slider .owl-dots .owl-dot:hover span {
  background: #2e7eed;
}
.about .about-slider .owl-dots .owl-dot.active span {
  background: #2e7eed;
}

.create-stories .block img {
  width: 100%;
  margin-bottom: 20px;
}
.create-stories .block h3 {
  margin-bottom: 10px;
}
@media (max-width: 768px) {
  .create-stories .block {
    margin-bottom: 30px;
  }
}

.quotes .quote-slider h2 {
  font-size: 50px;
}
.quotes .quote-slider cite {
  margin-left: 150px;
  font-style: normal;
}

.clients {
  padding: 50px 0;
}
.clients h3 {
  margin-bottom: 30px;
}
.clients .client-slider .slick-track {
  display: flex;
  align-items: center;
}
.clients .client-slider img {
  max-width: 80%;
}

.investors .block {
  margin-bottom: 30px;
}
.investors .block .image {
  margin-bottom: 20px;
}
.investors .block .image img {
  width: 100%;
  border-radius: 8px;
}
.investors .block h3 {
  margin-bottom: 0;
  line-height: 1;
}
.investors .block p {
  font-size: 14px;
}

.hover-zoom {
  overflow: hidden;
  border-radius: 8px;
}
.hover-zoom img {
  transition: 0.3s ease;
}
.hover-zoom:hover img {
  transform: scale(1.2);
}

.error-page {
  position: fixed;
  height: 100%;
  width: 100%;
}
.error-page .center {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.error-page .center .block h1 {
  font-size: 200px;
  font-weight: 400;
  line-height: 266px;
  font-family: "Lora", serif;
}
.error-page .center .block p {
  margin-bottom: 50px;
}

.career-featured .block {
  display: flex;
}
@media (max-width: 768px) {
  .career-featured .block {
    flex-wrap: wrap;
  }
}
.career-featured .block .content {
  flex-basis: 100%;
  align-self: center;
}
@media (max-width: 768px) {
  .career-featured .block .content {
    flex-grow: 1;
    width: 100%;
    margin-bottom: 30px;
    text-align: center;
  }
}
.career-featured .block .content h2 {
  margin-bottom: 30px;
}
.career-featured .block .video {
  justify-content: center;
  align-self: center;
  flex-basis: 100%;
  margin-left: 10px;
}
@media (max-width: 768px) {
  .career-featured .block .video {
    flex-grow: 1;
    width: 100%;
  }
}

.company-fun-facts h2 {
  margin-bottom: 60px;
}
.company-fun-facts .fun-fact {
  margin-bottom: 20px;
  text-align: center;
}
.company-fun-facts .fun-fact i {
  font-size: 25px;
  display: inline-block;
  margin-bottom: 10px;
  line-height: 60px;
  height: 60px;
  width: 60px;
  border: 1px solid #000;
  border-radius: 100%;
}

.gallery .image {
  cursor: pointer;
}

.job-list .block {
  padding: 50px 80px;
  background: #fff;
}
.job-list .block h2 {
  margin-bottom: 40px;
  font-size: 30px;
}
.job-list .block .job {
  padding: 50px 10px;
  display: flex;
}
@media (max-width: 768px) {
  .job-list .block .job {
    display: block;
    text-align: center;
  }
}
.job-list .block .job:not(:last-child) {
  border-bottom: 1px solid #cccccc;
}
@media (max-width: 480px) {
  .job-list .block .job {
    flex-wrap: wrap;
  }
}
.job-list .block .job .content {
  flex-basis: 100%;
}
.job-list .block .job .content h3 {
  margin-bottom: 0;
}
.job-list .block .job .apply-button {
  flex-basis: 100%;
  align-self: center;
  text-align: right;
}
@media (max-width: 768px) {
  .job-list .block .job .apply-button {
    margin-top: 20px;
    text-align: center;
  }
}

.faq .block {
  padding: 50px;
}
@media (max-width: 480px) {
  .faq .block {
    padding: 30px;
  }
}
.faq .block .faq-item {
  margin-bottom: 40px;
}
.faq .block .faq-item .faq-item-title {
  margin-bottom: 30px;
}
.faq .block .faq-item .faq-item-title h2 {
  font-size: 30px;
  border-bottom: 1px solid #cccccc;
}
.faq .block .faq-item .faq-item-title:last-child {
  margin-bottom: 0;
}
.faq .block .faq-item .item .item-link {
  position: relative;
  padding: 10px 0 10px 18px;
  padding-left: 25px;
}
.faq .block .faq-item .item .item-link a {
  font-size: 20px;
  color: #000;
}
.faq .block .faq-item .item .item-link a span {
  margin-right: 5px;
}
.faq .block .faq-item .item .item-link:before {
  font-family: "themify";
  content: "\e64b";
  position: absolute;
  left: 0;
  font-weight: 600;
  font-size: 15px;
  top: 15px;
}
.faq .block .faq-item .item .accordion-block {
  background: #fafafa;
}
.faq .block .faq-item .item .accordion-block p {
  padding: 20px;
}

.privacy .privacy-nav {
  position: -webkit-sticky;
  position: sticky;
  top: 15px;
  background: #fafafa;
  padding: 30px 0;
  display: flex;
  justify-content: center;
}
.privacy .privacy-nav ul {
  padding-left: 0;
  margin-bottom: 0;
}
.privacy .privacy-nav ul li {
  list-style: none;
}
.privacy .privacy-nav ul li a {
  font-size: 16px;
  color: #757575;
  padding: 10px 0;
  font-weight: bold;
  display: block;
}
@media (max-width: 768px) {
  .privacy .privacy-nav ul li a {
    font-size: 16px;
    padding: 5px 0;
  }
}
.privacy .privacy-nav ul li a.active {
  color: #000;
}
@media (max-width: 768px) {
  .privacy .privacy-nav {
    margin-bottom: 30px;
  }
}
.privacy .block {
  background: #fff;
  padding: 40px 50px;
}
.privacy .block .policy-item {
  padding-bottom: 40px;
}
.privacy .block .policy-item .title {
  margin-bottom: 20px;
}
.privacy .block .policy-item .title h3 {
  border-bottom: 1px solid #cccccc;
  padding-bottom: 15px;
}
.privacy .block .policy-item .policy-details p {
  margin-bottom: 20px;
}

.user-login {
  height: 100%;
  width: 100%;
}
.user-login .block {
  display: flex;
}
@media (max-width: 768px) {
  .user-login .block {
    flex-wrap: wrap;
  }
}
.user-login .block .image {
  flex-basis: 100%;
  margin-right: 40px;
}
@media (max-width: 768px) {
  .user-login .block .image {
    flex-grow: 1;
    text-align: center;
    margin-bottom: 30px;
    margin-right: 0;
  }
}
.user-login .block .image img {
  border-radius: 8px;
}
.user-login .block .content {
  flex-basis: 100%;
  align-self: center;
  padding: 50px;
  border: 1px solid #cccccc;
  border-radius: 4px;
}
@media (max-width: 768px) {
  .user-login .block .content {
    flex-grow: 1;
  }
}
.user-login .block .content .logo {
  margin-bottom: 80px;
}
@media (max-width: 992px) {
  .user-login .block .content .logo {
    margin-bottom: 40px;
  }
}
.user-login .block .content .title-text {
  margin-bottom: 35px;
}
.user-login .block .content .title-text h3 {
  padding-bottom: 20px;
  border-bottom: 1px solid #cccccc;
}
.user-login .block .content .new-acount {
  margin-top: 20px;
}
.user-login .block .content .new-acount p, .user-login .block .content .new-acount a {
  font-size: 14px;
}
.user-login .block .content .new-acount p a {
  color: #000;
}

.coming-soon {
  color: #000;
  padding: 120px 0;
  min-height: 100vh;
}
@media (max-width: 992px) {
  .coming-soon {
    padding: 80px 0;
  }
}
.coming-soon .block h3 {
  color: #808080;
}
.coming-soon .block .count-down {
  margin-top: 70px;
}
@media (max-width: 768px) {
  .coming-soon .block .count-down {
    margin-top: 40px;
  }
}
.coming-soon .block .count-down .syotimer-cell {
  min-width: 200px;
  padding: 45px 0;
  margin-right: 30px;
  margin-bottom: 20px;
  background: #fff;
  display: inline-block;
}
@media (max-width: 768px) {
  .coming-soon .block .count-down .syotimer-cell {
    min-width: 180px;
    padding: 35px 0;
  }
}
.coming-soon .block .count-down .syotimer-cell .syotimer-cell__value {
  font-size: 65px;
  line-height: 80px;
  text-align: center;
  position: relative;
  font-weight: bold;
}
.coming-soon .block .count-down .syotimer-cell .syotimer-cell__unit {
  font-size: 20px;
  color: #6c6c6c;
  text-transform: uppercase;
  font-weight: normal;
}

.address .block .address-block {
  text-align: center;
}
.address .block .address-block .icon {
  margin-bottom: 25px;
  display: flex;
  justify-content: center;
}
.address .block .address-block .icon i {
  display: block;
  height: 100px;
  width: 100px;
  background: #fafafa;
  border-radius: 100%;
  font-size: 45px;
  text-align: center;
  line-height: 100px;
}

.google-map {
  position: relative;
}
.google-map #map_canvas {
  height: 500px;
  width: 100%;
}
@media (max-width: 768px) {
  .google-map #map_canvas {
    height: 350px;
  }
}
/*# sourceMappingURL=style.css.map */
