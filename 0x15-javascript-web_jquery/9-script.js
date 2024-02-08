document.addEventListener("DOMContentLoaded", () =>
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", (data) =>
    $("DIV#hello").text(data.hello)
  )
);
