let script = document.createElement("script");
script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js";
script.type = "text/javascript";
document.head.appendChild(script);

script.onload = () => {
  tinymce.init({
    height: "480",
    selector: "#id_content",
    plugins: [
      "advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker",
      "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
      "table emoticons template paste help",
    ],
    toolbar:
      "undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | " +
      "bullist numlist outdent indent | link image | print preview media fullpage | " +
      "forecolor backcolor emoticons | help",
    menu: {
      favs: {
        title: "My Favorites",
        items: "code visualaid | searchreplace | spellchecker | emoticons",
      },
    },
    menubar: "favs file edit view insert format tools table help",
    content_css: "css/content.css",
  });
};
