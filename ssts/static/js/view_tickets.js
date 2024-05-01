// Get the edit buttons
const editButtons = document.querySelectorAll('.edit-btn');

// Get the edit modal
const editModal = document.getElementById('edit-modal');

// Get the save button
const saveButton = document.getElementById('save-btn');

// Add event listener to each edit button
editButtons.forEach((button) => {
  button.addEventListener('click', () => {
    // Get the incident id
    let incidentId = button.getAttribute('data-id');

    // Show the edit modal
    editModal.style.display = 'block';



	let incidentName = button.getAttribute('data-name');
	let incidentDescription = button.getAttribute('data-description');
    let incidentOS = button.getAttribute('data-os');
	let incidentWorker = button.getAttribute('data-worker');
	let incidentDevice = button.getAttribute('data-device');
    let incidentStatus = button.getAttribute('data-status');

    console.log(incidentOS)

    console.log(incidentId)
	
	// pass the incident name and description the text boxes to be autofilled

    //document.getElementById('incident-id').value = incidentId;
	document.getElementById('incident-name').value = incidentName;
	document.getElementById('incident-description').value = incidentDescription;
    document.getElementById('incident-os').value = incidentOS;
	document.getElementById('incident-worker').value = incidentWorker;
	document.getElementById('incident-device').value = incidentDevice;
    document.getElementById('incident-status').value = incidentStatus;
  });
});

// Add event listener to the save button
document.getElementById('save-btn').addEventListener('click', () => {
  // Get the incident id from the modal's data attribute
  const incidentId = document.getElementById('edit-modal').getAttribute('data-id');

  // Get the new incident name and description
  const incidentName = document.getElementById('incident-name').value;
  const incidentDescription = document.getElementById('incident-description').value;
  const incidentOS = document.getElementById('incident-os').value;
  const incidentWorker = document.getElementById('incident-worker').value;
  const incidentDevice = document.getElementById('incident-device').value;
  const incidentStatus = document.getElementById('incident-status').value;

    // Send the updated incident data to the server
    fetch(`/edit-incident/$<incidentId>`, {
      method: 'POST',
      body: JSON.stringify({
        id : incidentId,
        name: incidentName,
        description: incidentDescription,
        os: incidentOS,
        worker: incidentWorker,
        device: incidentDevice,
        status: incidentStatus,
      }),
      headers: {
        'Content-Type': 'application/json',
      },
    })
});