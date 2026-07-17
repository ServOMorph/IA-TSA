(function () {
  const input = document.getElementById("ecoute-input");
  const addBtn = document.getElementById("btn-ecoute-lire");
  const history = document.getElementById("ecoute-history");

  const PLAY_ICON =
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">' +
    '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>' +
    '<path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>' +
    '<path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>' +
    "</svg>";

  const EDIT_ICON =
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">' +
    '<path d="M12 20h9"/>' +
    '<path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>' +
    "</svg>";

  let entries = [];
  let nextId = 1;
  let currentAudio = null;

  function speakText(text) {
    if (!ActivityCore.settings.son || ActivityCore.settings.calme) {
      return Promise.resolve();
    }
    return fetch("/api/tts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text }),
    })
      .then(function (res) {
        if (!res.ok) throw new Error("tts_failed");
        return res.blob();
      })
      .then(function (blob) {
        if (currentAudio) {
          currentAudio.pause();
          URL.revokeObjectURL(currentAudio.src);
        }
        const url = URL.createObjectURL(blob);
        currentAudio = new Audio(url);
        return currentAudio.play();
      });
  }

  function render() {
    history.innerHTML = "";
    entries.forEach(function (entry) {
      const row = document.createElement("div");
      row.className = "ecoute-entry";
      row.dataset.id = entry.id;

      const text = document.createElement("span");
      text.className = "ecoute-entry-text";
      text.textContent = entry.text;

      const playBtn = document.createElement("button");
      playBtn.className = "ecoute-entry-btn";
      playBtn.setAttribute("aria-label", "Relire");
      playBtn.innerHTML = PLAY_ICON;
      playBtn.addEventListener("click", function () {
        playEntry(entry.id, playBtn);
      });

      const editBtn = document.createElement("button");
      editBtn.className = "ecoute-entry-btn";
      editBtn.setAttribute("aria-label", "Modifier");
      editBtn.innerHTML = EDIT_ICON;
      editBtn.addEventListener("click", function () {
        startEdit(entry.id, row);
      });

      row.appendChild(text);
      row.appendChild(playBtn);
      row.appendChild(editBtn);
      history.appendChild(row);
    });
    history.scrollTop = history.scrollHeight;
  }

  function playEntry(id, btn) {
    const entry = entries.find(function (e) { return e.id === id; });
    if (!entry || btn.disabled) return;
    btn.disabled = true;
    ActivityCore.logEvent("lecture", null);
    speakText(entry.text).finally(function () {
      btn.disabled = false;
    });
  }

  function startEdit(id, row) {
    const entry = entries.find(function (e) { return e.id === id; });
    if (!entry) return;

    row.innerHTML = "";
    const editInput = document.createElement("input");
    editInput.type = "text";
    editInput.className = "ecoute-entry-edit-input";
    editInput.value = entry.text;
    row.appendChild(editInput);
    editInput.focus();
    editInput.setSelectionRange(editInput.value.length, editInput.value.length);

    function commit() {
      const val = editInput.value.trim();
      if (val) {
        entry.text = val;
        ActivityCore.logEvent("modification", null);
      }
      render();
    }

    editInput.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        commit();
      } else if (e.key === "Escape") {
        e.preventDefault();
        render();
      }
    });
    editInput.addEventListener("blur", commit);
  }

  function addEntry() {
    const text = input.value.trim();
    if (!text || addBtn.disabled) return;

    const entry = { id: nextId++, text: text };
    entries.push(entry);
    input.value = "";
    render();
    ActivityCore.logEvent("ligne-ajoutee", null);

    addBtn.disabled = true;
    speakText(text).finally(function () {
      addBtn.disabled = false;
    });
  }

  addBtn.addEventListener("click", addEntry);
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      e.preventDefault();
      addEntry();
    }
  });
})();
