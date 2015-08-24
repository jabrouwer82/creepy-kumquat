$('#source-delete').click(function() {
  if(!confirm("Remove this source from the datastore?")) {
    event.preventDefault();
  }
});

