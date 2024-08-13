<template>
  <div>
    <h2>Sponsor Requests</h2>
    <table class="table table-dark">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Sponsor Name</th>
          <th scope="col">Company Name</th>
          <th scope="col">Industry</th>
          <th scope="col">Budget</th>
          <th scope="col">Status</th>
          <th scope="col">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="sponsor in sponsors" :key="sponsor.id">
          <td scope="row">{{ sponsor.sponsor_id }}</td>
          <td>{{ sponsor.sponsor_name}}</td>
          <td>{{ sponsor.company_name }}</td>
          <td>{{ sponsor.industry }}</td>
          <td>{{ sponsor.budget }}</td>
          <td>{{ sponsor.status }}</td>
          <td>
            <button @click="updateSponsorStatus(sponsor.sponsor_id, 'approved')" class="btn btn-success" style="font-size:12px;margin:4px"><i class="fa-solid fa-check"></i> Approve</button>
            <button @click="deleteSponsor(sponsor.sponsor_id)" class="btn btn-danger"  style="font-size:12px;margin:4px"><i class="fa-solid fa-xmark"></i> Reject</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SponsorRequest',
  data() {
    return {
      sponsors: [],
      user_id :"",
      user_name:"",
    };
  },
  methods: {
    fetchSponsorRequests() {
      axios.get('http://127.0.0.1:5000/api/sponsors', {
        headers: {
          'Authorization': localStorage.getItem('authToken')
        }
      })
      .then(response => {
        this.sponsors = response.data.data;
        this.user_id = response.data.data.user_id;
        
      })
      .catch(error => {
        console.error('Error fetching sponsor requests:', error);
      });
    },
    updateSponsorStatus(sponsorId, status) {
      axios.put(`http://127.0.0.1:5000/api/sponsor/${sponsorId}`, { status }, {
        headers: {
          'Authorization': localStorage.getItem('authToken')
        }
      })
      .then(response => {
        this.fetchSponsorRequests();
        alert('sponsor approved successfully')
      })
      .catch(error => {
        console.error(`Error updating sponsor status to ${status}:`, error);
      });
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

    deleteSponsor(sponsorId) {
      axios.delete(`http://127.0.0.1:5000/api/sponsor/${sponsorId}`, {
        headers: {
          'Authorization': localStorage.getItem('authToken')
        }
      })
      .then(response => {
        this.fetchSponsorRequests();
        alert('sponsor deleted successfully')
      })
      .catch(error => {
        console.error('Error deleting sponsor:', error);
      });
    }
  },
  created() {
    this.fetchSponsorRequests();
  }
};
</script>