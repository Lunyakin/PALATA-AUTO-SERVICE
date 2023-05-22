ClassicEditor
	.create( document.querySelector( '.editor' ) )
	.then( editor => {
		console.log( 'Editor was initialized', editor );
	} )
	.catch( err => {
		console.error( err.stack );
	} );
