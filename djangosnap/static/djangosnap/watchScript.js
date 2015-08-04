$( document ).ready(function () {
    console.log(mediaURLS);
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
                 $('#previous').css("visibility","visible")
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
         var height = $('#inercover').height();
         $('#vid').css("visibility","visible");
         $('#vid').width(width);
         $('#vid').height(height);
         $('#vid').attr('src', mediaURLS[currentMediaIndex]);
         $('#vid')[0].load();
     }

    function loadImage()
    {
        closeOutVideo();
        var width = $('#innercover').width();
        var height = $('#inercover').height();
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

function isVid(url)
{
  var extension = url.substr(url.length - 3);
  if (extension === 'mp3')
  {
    return true;
  }
  return false;
}
