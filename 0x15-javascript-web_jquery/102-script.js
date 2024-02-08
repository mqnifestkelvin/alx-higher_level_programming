document.addEventListener("DOMContentLoaded", () =>
  $("INPUT#btn_translate").click(() =>
    $.get(
      "https://www.fourtonfish.com/hellosalut/hello/?lang=" +
        $("INPUT#language_code").val(),
      (data) => $("DIV#hello").html(data.hello)
    )
  )
);
