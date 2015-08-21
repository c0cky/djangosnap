$( document ).ready(function () {
});

// console.log(mediaURLS);
    var currentMediaIndex = 0;
    var currentMediaURL = "";
    if (mediaURLS.length > 0)
    {
        currentMediaURL = mediaURLS[currentMediaIndex];
        if (mediaURLS.length > 1)
        {
            $('#next' ).css("visibility","visible");
        }
        loadMedia();


    }
     function previousMedia()
     {
         var temp = currentMediaIndex - 1;
         if (temp >= 0 )
         {
             if (temp == 0)
             {
                 $('#previous').css("visibility","hidden");
             }
             if (currentMediaIndex != 0) {
                $('#next').css("visibility","visible");
             }
             currentMediaIndex--;
             loadMedia();
         }

     }

     function nextMedia()
     {
         var temp = currentMediaIndex + 1;
         if (temp < mediaURLS.length)
         {
             if (temp == mediaURLS.length -1)
             {
                 $('#next').css("visibility","hidden");
             }
             if (currentMediaIndex == 0)
             {
                 $('#previous').css("visibility","visible");
             }
             currentMediaIndex++;
             loadMedia(currentMediaIndex);
         }

     }

    function loadMedia()
    {
        var vid = isVid(mediaURLS[currentMediaIndex]);
        if (vid)
        {
            loadVideo();
        }
        else
        {
            loadImage();
        }
    }

     function loadVideo()
     {
         closeOutImage();
         var width = $('#innercover').width();
         var height = 500;
        //  $('#vid').css("visibility","visible");
        //  player.dimensions(700, 450);
        // var player = videojs('vid');
        // player.src(mediaURLS[currentMediaIndex]);
        // player.load();
        // $('#vid_html5_api').width(width);
        // $('#vid_html5_api').height(height);

        // BV = new $.BigVideo();
        // BV.init();
        // BV.show(mediaURLS[currentMediaIndex],{ambient:true});
     }

    function loadImage()
    {
        closeOutVideo();
        var width = $('#innercover').width();
        var height = 450;
        $('#im').css("visibility","visible");
        $('#im').width(width);
        $('#im').height(height);
        $('#im').attr('src', mediaURLS[currentMediaIndex]);

    }

    function closeOutImage()
    {
        $('#im').css("visibility","hidden");
        $('#im').width(0);
        $('#im').height(0);
    }

    function closeOutVideo()
    {
        $('#vid').css("visibility","hidden");
        $('#vid').width(0);
        $('#vid').height(0);
    }
$("#vid").on("swipeleft",function(){
  previousMedia();
});
$("#vid").on("swiperight",function(){
  nextMedia();
});


$(document).keydown(function(e) {
    switch(e.which) {
        case 37: // left
        if ($('#previous').is(":visible")) {
            previousMedia();
        }
        break;

        case 38: // up
        break;

        case 39: // right
        if ($('#next').is(":visible")) {
            nextMedia();
        }
        break;

        case 40: // down
        break;

        default: return; // exit this handler for other keys
    }
    e.preventDefault(); // prevent the default action (scroll / move caret)
});


function isVid(url)
{
  var extension = url.substr(url.length - 3);
  if (extension === 'mp4')
  {
    return true;
  }
  return false;
}
