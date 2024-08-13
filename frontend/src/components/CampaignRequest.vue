<template>
  <div>
    <h2>Campaigns</h2>
    <table class="table table-dark">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Campaign Name</th>
          <th scope="col">Sponsor id</th>
          <th scope="col">start date</th>
          <th scope="col">End date</th>
          <th scope="col">Budget</th>
          <th scope="col">Status</th>
          <th scope="col">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="campaign in campaigns" :key="campaign.id">
          <td scope="row">{{ campaign.id }}</td>
          <td>{{ campaign.name}}</td>
          <td>{{ campaign.sponsor_id }}</td>
          <td>{{ formatDate(campaign.start_date) }}</td>
          <td>{{ formatDate(campaign.end_date) }}</td>
          <td>{{ campaign.budget }}</td>
          <td>{{campaign.status}}</td>
          <td>
            <button @click="updateCampaignStatus(campaign.id, 'approved')" class="btn btn-success" style="font-size:12px;margin:4px"><i class="fa-solid fa-check"></i> Approve</button>
            <button @click="deleteCampaign(campaign.id)" class="btn btn-danger"  style="font-size:12px;margin:4px"><i class="fa-solid fa-xmark"></i> Reject</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CampaignRequest',
  data() {
    return {
      campaigns: [],
      user_id :"",
      user_name:"",
    };
  },
  methods: {
    fetchCampaignRequests() {
      axios.get('http://127.0.0.1:5000/api/campaign', {
        headers: {
          'Authorization': localStorage.getItem('authToken')
        }
      })
      .then(response => {
        this.campaigns = response.data.data;
        this.user_id = response.data.data.user_id;
        
      })
      .catch(error => {
        console.error('Error fetching sponsor requests:', error);
      });
    },
    updateCampaignStatus(campaignId, status) {
      axios.put(`http://127.0.0.1:5000/api/campaignUpdate/${campaignId}`, { status }, {
        headers: {
          'Authorization': localStorage.getItem('authToken')
        }
      })
      .then(response => {
        this.fetchCampaignRequests();
        alert('campaign approved successfully')
      })
      .catch(error => {
        console.error(`Error updating sponsor status to ${status}:`, error);
      });
    },
    formatDate(dateStr) {
      const date = new Date(dateStr);
      const options = { year: 'numeric', month: 'long', day: '2-digit' };
      return date.toLocaleDateString(undefined, options);
    },
    fetchusername(id){
      const authToken = localStorage.getItem('authToken');
      axios.get(`http://127.0.0.1:5000/api/user/${id}`, {
        headers: {
          'Authorization': authToken,
        },
      })
      .then(response => {

        this.user_name = response.data.data.username;
      })
      .catch(error => {
        console.error('An error occurred while fetching the user:', error);
        this.error = 'An error occurred while fetching the influencers. Please try again.';
      });

    },

    deleteCampaign(campaignId) {
      axios.delete(`http://127.0.0.1:5000/api/campaign/${campaignId}`, {
        headers: {
          'Authorization': localStorage.getItem('authToken')
        }
      })
      .then(response => {
        this.fetchCampaignRequests();
        alert('sponsor deleted successfully')
      })
      .catch(error => {
        console.error('Error deleting sponsor:', error);
      });
    }
  },
  created() {
    this.fetchCampaignRequests();
  }
};
</script>