<template>
  <div class="sponsors-container" v-if="sponsors.length">
    <h2 style="color:#48cae4;font-style:bold;padding-bottom:10px;font-weight:800;font-size:40px;text-shadow: 2px 2px 5px #000;">All Sponsors</h2>
    <div class="sponsor-cards">
      <div class="sponsor-card" v-for="sponsor in sponsors" :key="sponsor.id">
        <div class="sponsor-content">
          <h3 style="background-color:#219ebc"><strong>{{ sponsor.company_name }}</strong></h3>
          <p><strong>Sponsor Name:</strong> {{ sponsor.sponsor_name }}</p>
          <p><strong>Budget:</strong> {{ formatBudget(sponsor.budget) }}</p>
          <p><strong>Industry:</strong> {{ sponsor.industry }}</p>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="no-sponsors">
    <p>No sponsors found.</p>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Sponsors',
  data() {
    return {
      sponsors: [],
      error: null,
      status:false,
    };
  },
  created() {
    this.fetchSponsors();
  },
  methods: {
    fetchSponsors() {
      const authToken = localStorage.getItem('authToken');
      axios.get('http://127.0.0.1:5000/api/sponsors', {
        headers: {
          'Authorization': `Bearer ${authToken}`,
        },
      })
      .then(response => {
        this.sponsors = response.data.data || [];
        this.status=sponsors.status;
      })
      .catch(error => {
        console.error('An error occurred while fetching the sponsors:', error);
        this.error = 'An error occurred while fetching the sponsors. Please try again.';
      });
    },
    formatBudget(budget) {
      return `${parseFloat(budget).toLocaleString()}`;
    },
  },
};
</script>

<style scoped>
.sponsors-container {
  padding: 20px;
}
.sponsor-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.sponsor-card {
  background-color: #faedcd;
  border: 1px solid #ddd;
  border-radius: 8px;
  width: calc(33.333% - 20px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 15px;
}
.sponsor-content {
  padding: 10px;
  font-size: 12px;
}
.no-sponsors {
  text-align: center;
  color: #999;
  padding: 20px;
}
</style>
