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
            goTo("employees");
        });
    },
    delete() {
        const url = `delete_employee/${this.employeeId.value}`;
        fetch(url).then((response) => {
            if (response.status === 500) {
                alert("Funcionário inexistente.");
            }
            goTo("employees");
        });
    }
}

const team = {
    name: document.getElementById("teamName"),
    teamId: document.getElementById("teamId"),
    add() {
        const url = `new_team?name=${this.name.value}`;
        fetch(url).then((response) => {
            goTo("teams");
        });
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
    recommender: document.getElementById("recommenderId"),
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
                alert("Time inexistente.");
            }
            goTo("recommendations");
        });
    }
}

const employeeToTeam = {
    employeeId: document.getElementById("ETEmployeeId"),
    teamId: document.getElementById("ETTeamId"),
    // employeeTeamId: document.getElementById("employeeTeamId"),
    add() {
        const url = `add_employee_to_team?employeeId=${this.employeeId.value}
                    &teamId=${this.teamId.value}`;
        fetch(url).then((response) => {
            if (response.status === 500) {
                alert("Funcionário e/ou time inválidos.");
            }
            goTo("teams");
        });
    }
    // remove() {
    //     const url = `remove_employee_from_team/${this.recommendationId.value}`;
    //     fetch(url).then((response) => {
    //         if (response.status === 500) {
    //             alert("Time inexistente.");
    //         }
    //         goTo("teams");
    //     });
    // }
}

function goTo(location) {
    window.location.href = `/${location}`;
}