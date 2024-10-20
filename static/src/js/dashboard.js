/** @odoo-module */

import { registry } from '@web/core/registry';

const { Component, onWillStart, useState } = owl;

import { jsonrpc } from "@web/core/network/rpc_service";

export class ProjectDashboard extends Component {
    setup() {
        this.project_state = useState({
            projects_count: 0,
            projects: []
        });

        onWillStart(this.onWillStart);
    }

    // Event
    async onWillStart() {
        await this.fetchDataProjectCount();
        await this.fetchProjectData();  // Fetch project data
    }

    // Fetch data from project count
    fetchDataProjectCount() {
        var self = this;
        jsonrpc("/project/dashboard/count", {}).then(function(data_result) {
            self.project_state.projects_count = data_result.projects_count;
        });
    }

    // Fetch project data
    fetchProjectData() {
        var self = this;
        jsonrpc("/project/dashboard/data", {}).then(function(data_result) {
            self.project_state.projects = data_result.projects;
        });
    }

    _onClickProjects() {
        var project_ids = this.project_state.project_ids;
        if (project_ids) {
            console.log(project_ids);
        }
    }
}

ProjectDashboard.template = "ProjectDashBoardMain";
registry.category("actions").add("project_dashboard_main", ProjectDashboard);
