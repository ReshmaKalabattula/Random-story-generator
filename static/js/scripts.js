// Function to fetch a new story from the server
async function fetchNewStory() {
    try {
        const response = await fetch('/new_story');
        if (response.ok) {
            const data = await response.json();  // Expecting JSON response
            document.querySelector('p').innerText = data.story;  // Update the paragraph with the new story
        } else {
            console.error('Failed to fetch new story.');
        }
    } catch (error) {
        console.error('Error fetching new story:', error);
    }
}

// Add event listener to the button
document.querySelector('button').addEventListener('click', fetchNewStory);
