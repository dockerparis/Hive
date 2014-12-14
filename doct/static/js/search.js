$(function() {
  $("#tasks_searck").autocomplete({
    source: "/search/task/",
    minLength: 2,
    select: function( event, ui) {
        console.log(ui.id);
        window.location.replace("/task/" + ui.item.id);
        console.log(event, ui);
        log( ui.item ?
            "Selected: " + ui.item.label :
            "Nothing selected, input was " + this.value);
      }
  });
});
