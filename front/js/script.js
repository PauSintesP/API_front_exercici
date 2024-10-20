fetch("http://127.0.0.1:8000/alumnes/llista")
    .then(response => {
        console.log("Resposta del servidor:", response); // Mostra la resposta del servidor
        if (!response.ok) {
            console.error("Error a la resposta del servidor", response.status); // Mostra el codi d'estat
            throw new Error("Error a la resposta del servidor");
        }
        return response.json();  // Converteix la resposta a JSON
    })
    .then(data => {
        console.log("Dades rebudes:", data);  // Mostra les dades rebudes

        if (!Array.isArray(data)) {
            throw new Error("La resposta no és una llista d'alumnes");
        }

        // Verifica si el DOM està trobant correctament l'element de la taula
        const alumnesTableBody = document.querySelector("#tablaAlumne tbody");
        if (!alumnesTableBody) {
            throw new Error("No s'ha trobat la taula o el tbody a l'HTML");
        }

        alumnesTableBody.innerHTML = "";  // Neteja la taula abans d'afegir-hi noves dades

        data.forEach(alumne => {
            console.log("Alumne:", alumne);  // Mostra cada alumne individualment per verificar el format

            const row = document.createElement("tr");

            const nomAluCell = document.createElement("td");
            nomAluCell.textContent = alumne.NomAlumne || 'Desconegut';
            row.appendChild(nomAluCell);

            const cicleAluCell = document.createElement("td");
            cicleAluCell.textContent = alumne.Cicle || 'Desconegut';
            row.appendChild(cicleAluCell);

            const cursAluCell = document.createElement("td");
            cursAluCell.textContent = alumne.Curs || 'Desconegut';
            row.appendChild(cursAluCell);

            const grupAluCell = document.createElement("td");
            grupAluCell.textContent = alumne.Grup || 'Desconegut';
            row.appendChild(grupAluCell);

            const descAulaCell = document.createElement("td");
            descAulaCell.textContent = alumne.DescAula || 'Desconegut';
            row.appendChild(descAulaCell);

            alumnesTableBody.appendChild(row);  // Afegeix la fila a la taula
        });
    })
    .catch(error => {
        console.error("Error capturat:", error);  // Mostra l'error a la consola
        alert("Error al carregar la llista d'alumnes");  // Afegeix una alerta per avisar l'usuari
    });
