<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="https://www.w3.org/1999/xhtml">
<head>
  <title>Marathi Dating - Free Marathi Dating - Register FREE</title>
  <meta name="description" content="Marathi Dating - Free Marathi Dating - Register for FREE, Marathimatrimony.com - Free matrimonials add your profile." />
<meta name="keywords" content="Indian matrimony, free matrimonial, Add Profile, matrimonials, Telugu, tamil, sindhi, assamese, gujarati, malayalee, hindu, christian, muslim, register profile, matrimonial, add profile, success stories, search profiles, matrimonial website, Indian matrimony, marwadi, oriya, kannada, hindi, Free matrimonials, matrimony, desi match maker, match maker, online matrimony" />
<link rel="shortcut icon" type="image/x-icon" href="https://imgs.marathidating.com/bmimages/faviconnew.ico" />
<meta name="robots" content="index, follow">
<meta name="robots" content="noarchive">
<link rel="icon" type="image/ico" href="https://imgs.marathidating.com/bmimages/faviconnew.ico" />
<link href="https://imgs.marathidating.com/bmstyles/jquery-ui-1.8.14.custom.css" rel="stylesheet" type="text/css" />
<link href="https://imgs.marathidating.com/bmstyles/fileUploader.css" rel="stylesheet" type="text/css" />
<link href="https://imgs.marathidating.com/bmstyles/reg-bootstrap-photo.css" rel="stylesheet" type="text/css">
<link href="https://imgs.marathidating.com/bmstyles/mainstyle.css" rel="stylesheet" type="text/css">
<link href="https://imgs.marathidating.com/bmstyles/reg-style.css" rel="stylesheet" type="text/css">
<style type="text/css">
.ui-button-text{padding:4px;}
.ui-button{height: 28px;width: 124px;}

#colorbox{min-height:100px !important;max-height:500px !important;}#cboxMiddleLeft{min-height:100px !important;max-height:500px !important;}#cboxContent{min-height:100px !important;max-height:500px !important;}#cboxLoadedContent{min-height:100px !important;max-height:500px !important;}#cboxMiddleRight{min-height:100px !important;max-height:500px !important;}

</style>
<script language="javascript" src="https://imgs.marathidating.com/scripts/jquery.js?random=180719103701"></script> 
<script language="javascript" src="https://imgs.marathidating.com/scripts/colorbox.js?random=180719103701"></script>
<script language="javascript" src="https://imgs.marathidating.com/scripts/common.js?rand=180719103701"></script> 
<script language="javascript" src="https://imgs.marathidating.com/scripts/photoadd.js?rand=180719103701"></script> 
<script language="javascript" src="https://imgs.marathidating.com/scripts/photo_common.js?rand=180719103701"></script> 
<script src="https://imgs.marathidating.com/scripts/jquery-ui-1.8.17.custom.min.js?rand=180719103701" type="text/javascript"></script> 
<script src="https://imgs.marathidating.com/scripts/jquery.fileUploader_inter.js?rand=180719103701" type="text/javascript"></script>
<script src="https://imgs.marathidating.com/scripts/jquery.fileUploader.js?rand=180719103701" type="text/javascript"></script>
<script type="text/javascript" language="javascript" src="https://imgs.marathidating.com/scripts/reggatrack.js?random=190220221213"></script>
<script type="text/javascript">
function cdtime(container, targetdate){
  if (!document.getElementById || !document.getElementById(container)) return;
  this.container=document.getElementById(container);
  this.currentTime=new Date('Wed July 30 2025 16:26:09');  //Thu Jul 05 2012 13:41:07 GMT+0530 (India Standard Time)   
  this.targetdate=new Date(targetdate);
  this.timesup=false;
  this.updateTime();
}
cdtime.prototype.updateTime=function(){
  var thisobj=this;
  this.currentTime.setSeconds(this.currentTime.getSeconds()+1);
  setTimeout(function(){thisobj.updateTime()}, 1000); //update time every second
}

cdtime.prototype.displaycountdown=function(baseunit, functionref){
  this.baseunit=baseunit;
  this.formatresults=functionref;
  this.showresults();
}

cdtime.prototype.showresults=function(){
  var thisobj=this;
  var timediff=(this.targetdate-this.currentTime)/1000 //difference btw target date and current date, in seconds
  if (timediff<0){ //if time is up
    this.timesup=true;
    this.container.innerHTML=this.formatresults();
    return;
  }
  var oneMinute=60; //minute unit in seconds
  var oneHour=60*60; //hour unit in seconds
  var oneDay=60*60*24; //day unit in seconds
  var dayfield=Math.floor(timediff/oneDay);
  var hourfield=Math.floor((timediff-dayfield*oneDay)/oneHour);
  var minutefield=Math.floor((timediff-dayfield*oneDay-hourfield*oneHour)/oneMinute);
  var secondfield=Math.floor((timediff-dayfield*oneDay-hourfield*oneHour-minutefield*oneMinute));

  if (this.baseunit=="hours"){ //if base unit is hours, set "hourfield" to be topmost level
    hourfield=dayfield*24+hourfield;
    dayfield="n/a";
  }
  else if (this.baseunit=="minutes"){ //if base unit is minutes, set "minutefield" to be topmost level
    minutefield=dayfield*24*60+hourfield*60+minutefield;
    dayfield=hourfield="n/a";
  }
  else if (this.baseunit=="seconds"){ //if base unit is seconds, set "secondfield" to be topmost level
    var secondfield=timediff;
    dayfield=hourfield=minutefield="n/a";
  }
  this.container.innerHTML=this.formatresults(dayfield, hourfield, minutefield, secondfield);
  setTimeout(function(){thisobj.showresults()}, 1000); //update results every second
}

function formatresults(){  
  if(arguments[1]<=0 && arguments[2]<=15 && arguments[3]==0)
  {
    getJsonData(arguments[2]);
  }
  if (this.timesup==false){//if target date/time not yet met
    var displaystring="You have <span style='font: normal 28px arial;color:#e13f3f;'>"+arguments[1]+"</span>hr <span style='font: normal 28px arial;color:#e13f3f;'>"+arguments[2]+"</span>min <span style='font: normal 28px arial;color:#e13f3f;'>"+arguments[3]+"</span>sec left, ";
  }
  else{ //else if target date/time met
    var displaystring="you have <span style='font: normal 28px arial;color:#e13f3f;'>0</span>hr <span style='font: normal 28px arial;color:#e13f3f;'>0</span>min <span style='font: normal 28px arial;color:#e13f3f;'>0</span>sec left	";
  }
  return displaystring;
}
</script>

<script type="text/javascript">
    $(function($){
      $('.fileUpload').fileUploader({'autoUpload':true,'limit':40,'lastestAddImageNumber':4,'url':'addphoto.php','site_url':'https://image.marathidating.com/photo/managephoto.php','overallcount':40});
    });
</script> 
<script>

  $(document).ready(function(){
    $('#addmycomp, #addmyfb').addClass('animated swing bounceIn');
  });

function phtobrw(){
  document.getElementById('browse').click();



}
</script>

</head>
<body>
<input type="hidden" name="skipphotono" id="skipphotono" value="0"/>
<div id="register-form" style="background: #fff;">
<!-- header start-->
   <div class="header_background paddb20" style="background-color: #fff;">
   <div class="container reg_header">
     <div class="row">
       <div class="col-sm-2 custom_resp_head_left" style="padding-top: 5px"><img src="https://imgs.marathidating.com/bmimgs/small_logo_bm.png" /></div>
       <div class="col-sm-9 biggertxt reg_color1" align="right" style="padding-top: 25px" >Add photos</div>
     </div>
   </div><br clear="all"/>
   </div>
   <div class="reg_header_bottom">  </div>
   <!-- header end-->

   <!--- container start-->
   <div class="container">
     <div class="row paddt30">
       <div class="col-md-12 hdtxt1" align="center" style="line-height: 24px;font-size: 18px;">
        Add a minimum of 3 photos to ensure your profile gets featured on top of the search results. 
       </div>
     </div>


     <div class="row paddb20">
     <div class="col-md-2"> </div>
     <form>
     <div class="col-md-3" align="center" id="addphoto-pge" style="padding-top:45px;">

            <a href="javascript:;" onclick="phtobrw();AddphotoGA('secndpg','AddPhotoLogo-Clicked');photouploadga('F','AddPhotoLogo-Clicked');">

     <img src="https://imgs.marathidating.com/bmimgs/inter-add-photo.png" width="85%" class="img-responsive"/>
     </div>
     <div class="col-md-5" >
      <div class="row"> 
    <div class="col-md-9">     

          <div class="row" align="center">
          <div class="col-md-12" >

        <input type="hidden" id="drag_val" value="0">
        <input type="hidden" id="dragged_uploaded" value="0">
        <input type="hidden" id="dragged_photo_no" value="1">
        <input type ="hidden" name ="firstphoto" id ="firstphoto" value = "1"/>
                      <div role="button" style="width:1px; height:1px;margin:0px;padding:0px;">
            <form action="addphoto.php?multiple=1&ID=" method="post" enctype="multipart/form-data">
              <div id="drag1_1">
              <input type="file" name="PHOTO1" id="browse" class="fileUpload" multiple style="visibility:hidden;">
              </div>
            </form>
            </div><div class="clear"></div>
            <div role="button" style="width:1px; height:1px;margin:0px;padding:0px;">
              <form action="addphoto.php?multiple=1&ID=" method="post" enctype="multipart/form-data">
              <div id="addphoto_link"><input type="file" name="PHOTO1" id="browse" class="fileUpload" style="width:120px; visibility:hidden;" multiple></div>
              </form>
            </div><div class="clear"></div>
                <a href="javascript:;" style="font-size:16px;text-decoration:none;display:inline-block; border-radius:6px;" id="addmycomp" class="relative" onclick="phtobrw();AddphotoGA('secndpg','AddPhotoNow-Clicked');photouploadga('F','AddPhotoNow-Clicked');">

        <div><button type="button" class="btn btn-complete-profile" style="background: #F68121;border: 1px solid #F68121;padding: 9px 33px;font-size: 14px;">ADD PHOTOS NOW</button> </div></a>
        <div class="footer_part paddt5 mediumtxt" style="font-size: 9px">Image size 15MB. jpeg/gif/png/bmp </div>
        </div>
      </div>
    </form>	



      <!-- <div class="row fb_margin_addphoto" >
          <div class="col-md-12  mediumtxt" ><img src="https://imgs.marathidating.com/bmimgs/facebook_newregs_form.png" align="left" style="margin-right:5px"/>  
                  <a href="javascript:;" style="text-decoration:none; display:inline-block;" onclick="AddphotoGA('secndpg','Select FB-Clicked');window.open('https://image.marathidating.com/photo/fbphotolist.php?ID=', 'Facebook_Connect', 'resizable=1,width=600,height=300');" id="addmyfb">
                  Select photos</a> from your Facebook account    <span class="reg_color1">(We'll never post anything on your wall)</span></div>
          <div class="clear paddb20"> </div>
      </div> -->

      </div>   </div>
     </div>

  <!-- START Female Safety Promotion-->
    <br><br>
  <div style="float: none;overflow: hidden;margin: 0 auto;background:#FFF1EE;  width: 832px; height: 110px; border-radius: 10px;">
    <div style="float: left; padding-left: 42px;padding-top:13px;"><img src="https://imgs.mobileshop.com/bmimgs/syspop-imgs/fs-payment-img.png"></div>
    <div style="padding: 29px 0 0 155px;">
      <div style="font-size: 16px;letter-spacing: 0.48px;line-height: 20px;color:#000000;width:565px;">When it comes to your safety, we are <span style="color: #d44949;">#AsCaringAsFamily</span>. You can always control who’ll be able to view your photos!
      </div>
    </div>
  </div>
    <!-- END Female Safety Promotion-->

  <div class="col-md-2"> </div>
     </div>
     <div class="clear"> </div>
     <div class="will_do_btn paddt30">
        <div align="right"><a href="javascript:void(0);" onclick="skipclosepopup();" style="text-decoration:none;"><button type="button" class="btn btn-default will_do_color" > I'll do this later &nbsp;&nbsp;> </button></a>  </div>
        </div>

   </div>
   <div style="height: 30px;"> </div>




   <!--- container end-->
<!-- Popup -->
<div style="display:none;">
<div id="confirmationcontent" style="width:530px;" class="paddl20 paddr20paddb20">
  <div class="boldtxt paddb20 txtopac" style="font-size:24px; padding-top:20px; color:#363636;">Are you sure?</div>
  <div class="txtopac" style="font-size:16px; color:#777;">If you don't upload your photo now, potential matches may not contact you.</div><div class="clear"></div><br/>
    <a onclick="AddphotoGA('secndpg','skip-dontwantbtn');regInterGA('AddPhoto','AddPhoto-SkipThisPage-IDont','marathi','R0XEBCC818');" href="https://image.marathidating.com/photo/managephoto.php"><span style="background: none repeat scroll 0 0 #f4f4f4; border: 1px solid #e4e4e4; border-radius: 4px; box-shadow: 1px 1px 1px #fff inset; color: #0274cb; cursor: pointer; font: 13px arial; padding: 10px 13px; text-decoration: none;" class="fleft txtopac">I am Fine With Less Responses</span></a>
    <a href="javascript:void(0)" onclick="AddphotoGA('secndpg','skip-addphotobtn'); $.colorbox.close();"><span style="border:1px solid #ff7805; background:#ff7805; padding:10px 20px;color:#4baa26; border-radius:3px; color:#FFF; font-weight:bold; font-size:16px; margin-left:10px;cursor: pointer;" class="fleft">Let Me Add My Photo</span></a>
<div class="clear"></div><br/>
</div>
</div>
<div class="clear"></div>
  <!-- footer -->
  <div class="container">
    <div class="reg_header_bottom paddt10 paddb10">  </div>
  <div align="center" class="paddt20 paddb20 footer_part">Copyright &copy; 2025. All rights reserved.  </div>
  <div class="paddt30 paddb20">  </div>
  </div>
  <!-- footer end -->
  </div>
</body>
</html>
  <script type="text/javascript">
  function skipclosepopup(){
     $.colorbox({inline:true,href:'#confirmationcontent',onClosed:function(){}}); 
  }

  $('#js-facebook-link').click(function(e) {
      $(this).colorbox({
            'href': $(this).attr('href'),						
            onClosed:function(){ 
            window.location='https://image.marathidating.com/photo/managephoto.php';	
            } 
      });
    }); 
</script>


<!-- Google Analytics Scripts starts -->
<script type="text/javascript">
$(document).ready(function(){
  AddphotoGAonload('secndpg','opened');
  regInterGA('AddPhoto','Addhoto-Viewed','marathi','R0XEBCC818');
});
function AddphotoGAonload(GASRC,GAACT)
{

      var category = 'REGPHOTO-marathi';


  _gaq.push(['_trackEvent',category, GASRC, GAACT,,true]); 
  ga('send', {'hitType': 'event', 'eventCategory': category, 'eventAction': GASRC, 'eventLabel': GAACT});
}
function AddphotoGA(GASRC,GAACT)
{

      var category = 'REGPHOTO-marathi';

  _gaq.push(['_trackEvent',category, GASRC, GAACT]); 	
  ga('send', {'hitType': 'event', 'eventCategory': category, 'eventAction': GASRC, 'eventLabel': GAACT});
}

<!-- Begin Consolidated GA Tracking -->
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-33448923-13', 'auto');
  ga('send', 'pageview');
<!-- End Consolidated GA Tracking -->

  $('#js-facebook-link').click(function(e){
      $(this).colorbox({
              'href': $(this).attr('href'),						
              onClosed:function(){ 
              window.location='https://image.marathidating.com/photo/managephoto.php';	
              } 
      });
    }); 
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', "UA-R0XEBCC818-1"]);
  _gaq.push(['_setDomainName', "marathidating.com"]);
    _gaq.push(["_setCustomVar", 1, "User", "M", 2]); 
    _gaq.push(["_setCustomVar", 2, "Member", "F", 2]);        
    _gaq.push(["_setCustomVar", 3, "Gender", "FF", 2]);
    _gaq.push(['_trackPageview']);
  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
  ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>

<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-R0XEBCC818"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){ dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-R0XEBCC818');
    function ga(se,ev,category,gamodule,action,nan){
      if(se=='send'){ 
        gtag('event',category,{'event_category':action,'event_label':gamodule});
      }
    }
    function gaq(){ 
      this.push = function(ev){
        if(ev[0]=='_trackEvent'){
          gtag('event',ev[1],{'event_category':ev[2],'event_label':ev[3]});	
        }	
      }
    }
    var _gaq = new gaq();
  </script>
<!-- Google Analytics Scripts ends -->
