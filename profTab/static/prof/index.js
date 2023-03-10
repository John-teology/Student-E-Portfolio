// document.addEventListener("DOMContentLoaded", () => {
//   document.querySelector("#addSubjectForm").addEventListener("submit", addSub);
// });

// addSub = (e) => {
//   e.preventDefault();
//   fetch("/professor/addSub/", {
//     method: "POST",
//     body: JSON.stringify({
//       subjectCode: document.querySelector("#subjectCode").value,
//       subjectName: document.querySelector("#subjectName").value,
//       facultyName: document.querySelector("#facultyName").value,
//       units: document.querySelector("#units").value,
//     }),
//   }).then((response) => {
//     document.querySelector("#subjectCode").value = "";
//     document.querySelector("#subjectName").value = "";
//     document.querySelector("#facultyName").value = "";
//     document.querySelector("#units").value = "";
//     alert("New Subject added!");
//     return response;
//   });
// };

$(document).on("submit", "#addSubjectForm", (e) => {
  e.preventDefault();
  $.post("/professor/addSub/", {
    subjectCode: $("#subjectCode").val(),
    subjectName: $("#subjectName").val(),
    facultyName: $("#facultyName").val(),
    units: $("#units").val(),
  }).then((response) => {
    clearInputs();
    $("#table").load(location.href + " #table"); // space is needed
  });
});

const clearInputs = () => {
  $("#subjectCode").val = "";
  $("#subjectName").val = "";
  $("#facultyName").val = "";
  $("#units").val = "";
};

// $(document).ready(() => {
//   const table = document.querySelector("#table");
//   fetch("/professor/subjects")
//     .then((response) => response.json())
//     .then((data) => {
//       data.forEach((d) => {
//         const view = document.createElement("div");
//         view.innerHTML = `
//         <h4>${d.subjectCode}</h4>
//         <h3>${d.subjectName}</h3>
//         `;
//         table.append(view);
//       });
//     });
// });
