// Get JQuery elements
const $search = $('#search')
const $room = $('#room')
const $results = $('#results')

/**
 * Loads filtered items into the results div
 */
function load_results() {
    // Get form values and URI-encode them
    const room = encodeURIComponent($room.val())
    const name = encodeURIComponent($search.val())

    // Load data into the div
    $results.load(`/filtered?name=${name}&room=${room}`)
}

// Automatic load results when the form input changes
$room.on('change',load_results)
$search.on('input',load_results)
$(document).ready(load_results)