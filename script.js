function addTask() {
    let input = document.getElementById("taskInput");
    let task = input.value.trim();

    if (task === "") return; // ignore empty input

    // Create list item
    let li = document.createElement("li");

    // Create checkbox
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";

    // Task text
    let span = document.createElement("span");
    span.textContent = task;

    // Toggle complete when checkbox is clicked
    checkbox.onclick = function() {
        li.classList.toggle("completed");
    };

    // Delete button
    let delBtn = document.createElement("button");
    delBtn.textContent = "Delete";
    delBtn.className = "delete-btn";
    delBtn.onclick = function() {
        li.remove();
    };

    // Append elements
    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(delBtn);

    document.getElementById("taskList").appendChild(li);

    input.value = ""; // clear input
}
