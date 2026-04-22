function addtask() {
    let input = document.getElementById("taskInput");
    let task = input.value.trim();

    if (task === "") return; // ignore empty input

    let li = document.createElement("li");
    li.textContent = task;

    // Add delete button
    let delBtn = document.createElement("button");
    delBtn.textContent = "Delete";
    delBtn.onclick = function() {
        li.remove();
    };

    // Add complete toggle
    li.onclick = function() {
        li.style.textDecoration = 
            li.style.textDecoration === "line-through" ? "none" : "line-through";
    };

    li.appendChild(delBtn);
    document.getElementById("taskList").appendChild(li);

    input.value = ""; // clear input
}
