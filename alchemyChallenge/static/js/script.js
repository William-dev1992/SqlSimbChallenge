const employee = {
    name: document.getElementById("employeeName"),
    email: document.getElementById("employeeEmail"),
    recommendedBy: document.getElementById("employeeRecommender"),
    employeeId: document.getElementById("employeeId"),
    add() {
        const url = `new_employee?name=${this.name.value}&email=${this.email.value}&recommendedBy=${this.recommendedBy.value}`;
        fetch(url).then((response) => {
            if (response.status === 500) {
                alert("Funcionário recomendador inválido.");
            }
            goTo("");
        });
    },
    delete() {
        const url = `delete_employee/${this.employeeId.value}`;
        fetch(url).then((response) => {
            if (response.status === 500) {
                alert("Funcionário inexistente.");
            }
            goTo("");
        });
    },
    countRecommendations() {
        const url = `count_recommendations/${this.employeeId.value}`;
        fetch(url)
            .then(response => {
                if (response.status === 500) {
                    alert("Funcionário inexistente.");
                } else {
                    return response.json();
                }
            }).then(response => {
                alert(`Total de recomendações: ${response.count}`);
                goTo("");
            });
    }
}

const team = {
    name: document.getElementById("teamName"),
    teamId: document.getElementById("teamId"),
    add() {
        if (this.name) {
            const url = `new_team?name=${this.name.value}`;
            fetch(url).then((response) => {
                goTo("teams");
            });
        } else {
            alert("O nome da equipe é necessário!")
        }
    },
    delete() {
        const url = `delete_team/${this.teamId.value}`;
        fetch(url).then((response) => {
            if (response.status === 500) {
                alert("Time inexistente.");
            }
            goTo("teams");
        });
    }
}

const recommendation = {
    recommender: document.getElementById("recommender"),
    recommendationId: document.getElementById("recommendationId"),
    recommendedName: document.getElementById("recommendedName"),
    recommendedEmail: document.getElementById("recommendedEmail"),
    add() {
        const url = `new_recommendation?recommender=${this.recommender.value}
                    &recommendedName=${this.recommendedName.value}
                    &recommendedEmail=${this.recommendedEmail.value}`;
        fetch(url).then((response) => {
            if (response.status === 500) {
                alert("Funcionário recomendador inválido.");
            }
            goTo("recommendations");
        });
    },
    delete() {
        const url = `delete_recommendation/${this.recommendationId.value}`;
        fetch(url).then((response) => {
            if (response.status === 500) {
                alert("Recomendação inexistente.");
            }
            goTo("recommendations");
        });
    }
}

const employeeToTeam = {
    employeeId: document.getElementById("ETEmployeeId"),
    teamId: document.getElementById("ETTeamId"),
    employeeTeamId: document.getElementById("employeeTeamId"),
    add() {
        const url = `new_team_employee?employeeId=${this.employeeId.value}
                    &teamId=${this.teamId.value}`;
        fetch(url).then((response) => {
            if (response.status === 500) {
                alert("Funcionário e/ou time inválidos.");
            }
            goTo("team_employees");
        });
    },
    delete() {
        const url = `delete_employee_from_team/${this.employeeTeamId.value}`;
        fetch(url).then((response) => {
            if (response.status === 500) {
                alert("Vínculo inexistente.");
            }
            goTo("team_employees");
        });
    }
}

const modal = {
    openModal(htmlClass) {
        const modal = document.querySelector(`.${htmlClass}`);
        modal.classList.remove('hidden');
    },
    closeModal(htmlClass) {
        const modal = document.querySelector(`.${htmlClass}`);
        modal.classList.add('hidden');
    }
}

function goTo(location) {
    window.location.href = `/${location}`;
}