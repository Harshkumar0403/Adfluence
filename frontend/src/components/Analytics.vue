<template>
  <div>
    <h2 style="color:#48cae4; font-weight:800; font-size:40px; text-shadow: 2px 2px 5px #000;">Analytics Dashboard</h2>
    <div class="stats-container">
      <span>Total Sponsors: {{ totalSponsors }}</span>
      <span>Total Influencers: {{ totalInfluencers }}</span>
      <span>Total Campaigns: {{ totalCampaigns }}</span>
      <span>Total Ads: {{ totalAds }}</span>
      <span>Total Budget: {{ totalBudget }}</span>
    </div>
    <div class="charts-container">
      
      <div class="chart-card">
        <h4>Sponsor's Budget</h4>
        <canvas id="sponsorBudgetChart"></canvas>
      </div>
      <div class="chart-card">
        <h4>Influencer's Reach</h4>
        <canvas id="influencerReachChart"></canvas>
      </div>
      <div class="chart-card">
        <h6>Categories</h6>
        <canvas id="categoryCountChart"></canvas>
      </div>
      <div class="chart-card">
        <h4>Active Days</h4>
            <canvas id="loginDayChart"></canvas>
          </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

export default {
  name: 'Analytics',
  data() {
    return {
      totalSponsors: 0,
      totalInfluencers: 0,
      totalCampaigns: 0,
      totalAds: 0,
      totalBudget: 0,
      sponsorBudgetData: [],
      influencerReachData: [],
      categoryCountData: [],
      campaignAdCountData: [],
      userLoginData: [],
      loginDayData: [],
      authToken:localStorage.getItem('authToken')
    };
  },
  methods: {
    fetchData() {
      axios.get('http://127.0.0.1:5000/api/sponsors',{
         headers: {
          'Authorization': this.authToken,
        },
      })
        .then(response => {
          const sponsors = response.data.data;
          if (Array.isArray(sponsors)) {
            this.totalSponsors = sponsors.length;
            this.totalBudget = sponsors.reduce((sum, sponsor) => sum + sponsor.budget, 0);
            this.sponsorBudgetData = sponsors;
            this.renderSponsorBudgetChart();
          } else {
            console.error('Sponsors data is not an array:', sponsors);
          }
        })
        .catch(error => console.error('Error fetching sponsors:', error));

      axios.get('http://127.0.0.1:5000/api/influencers',{
         headers: {
          'Authorization': this.authToken,
        },
      })
        .then(response => {
          const influencers = response.data.data;
          console.log(influencers)
          if (Array.isArray(influencers)) {
            this.totalInfluencers = influencers.length;
            this.influencerReachData = influencers;
            this.categoryCountData = this.countCategories(influencers);
            this.renderInfluencerReachChart();
            this.renderCategoryCountChart();
          } else {
            console.error('Influencers data is not an array:', influencers);
          }
        })
        .catch(error => console.error('Error fetching influencers:', error));

      axios.get('http://127.0.0.1:5000/api/campaign',{
         headers: {
          'Authorization': this.authToken,
        },
      })
        .then(response => {
          const campaigns = response.data.data;
          if (Array.isArray(campaigns)) {
            this.totalCampaigns = campaigns.length;
            this.fetchAdCounts(campaigns);
          } else {
            console.error('Campaigns data is not an array:', campaigns);
          }
        })
        .catch(error => console.error('Error fetching campaigns:', error));
        axios.get('http://127.0.0.1:5000/api/users',{
          headers: {
          'Authorization': this.authToken,
        },
        })
        .then(response => {
          const users = response.data.data;
          if (Array.isArray(users)) {
          this.processLoginData(users);
          this.renderLoginDayChart();
          } else {
            console.error('Users data is not an array:', users);
          }
        })
        .catch(error => console.error('Error fetching users:', error));

      axios.get('http://127.0.0.1:5000/api/Ad',{
         headers: {
          'Authorization': this.authToken,
        },
      })
        .then(response => {
          const ads = response.data.data;
          if (Array.isArray(ads)) {
            this.totalAds = ads.length;
          } else {
            console.error('Ads data is not an array:', ads);
          }
        })
        .catch(error => console.error('Error fetching ads:', error));
    },
     processLoginData(users) {
      const loginDayCount = { 'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0 };
      users.forEach(user => {
        const loginDate = new Date(user.current_login_at);
        const dayOfWeek = loginDate.toLocaleString('en-US', { weekday: 'long' });
        loginDayCount[dayOfWeek]++;
      });
      this.loginDayData = Object.entries(loginDayCount).map(([day, count]) => ({ day, count }));
    },
    fetchAdCounts(campaigns) {
      const campaignAdCounts = campaigns.map(campaign => {
        return {
          campaignName: campaign.name,
          adCount: campaign.ads ? campaign.ads.length : 0
        };
      });
      this.campaignAdCountData = campaignAdCounts;
      this.renderCampaignAdCountChart();
    },
    countCategories(influencers) {
      const categoryCount = {};
      influencers.forEach(influencer => {
        const category = influencer.category;
        if (category) {
          if (categoryCount[category]) {
            categoryCount[category]++;
          } else {
            categoryCount[category] = 1;
          }
        } else {
          console.error('Influencer category is undefined:', influencer.category);
        }
      });
      return Object.entries(categoryCount).map(([category, count]) => ({ category, count }));
    },
    renderSponsorBudgetChart() {
     const ctx = document.getElementById('sponsorBudgetChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.sponsorBudgetData.map(data => data.company_name),
          datasets: [{
            label: 'Budget',
            data: this.sponsorBudgetData.map(data => data.budget),
            backgroundColor: 'rgba(75, 192, 192, 0.8)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          },
          plugins: {
            datalabels: {
              anchor: 'end',
              align: 'top',
              formatter: Math.round,
              font: {
                weight: 'bold'
              }
            }
          }
        }
      });
    },
    renderInfluencerReachChart() {
      const ctx = document.getElementById('influencerReachChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.influencerReachData.map(data => data.influencer_name),
          datasets: [{
            label: 'Reach',
            data: this.influencerReachData.map(data => data.reach),
            backgroundColor: 'rgba(153, 102, 255, 0.8)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    },
    renderLoginDayChart() {
      const ctx = document.getElementById('loginDayChart').getContext('2d');
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: this.loginDayData.map(data => data.day),
          datasets: [{
            label: 'Active Days',
            data: this.loginDayData.map(data => data.count),
            backgroundColor: 'rgba(75, 192, 192, 0.7)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
            datalabels: {
              align: 'end',
              anchor: 'end'
            },
            fill: {
                target: 'origin',
                above: 'rgb(255, 0, 0,0.2)',   // Area will be red above the origin
                below: 'rgb(0, 0, 255,0.2)'    // And blue below the origin
              }
          }]
        },
        options: {
          plugins: {
            datalabels: {
              formatter: (value) => value
            }
          }
        }
      });
    },

    renderCategoryCountChart() {
      const ctx = document.getElementById('categoryCountChart').getContext('2d');
      new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: this.categoryCountData.map(data => data.category),
          datasets: [{
            label: 'Category Count',
            data: this.categoryCountData.map(data => data.count),
            backgroundColor: [
              'rgba(255, 99, 132,0.5)',
              'rgba(54, 162, 235,0.5)',
              'rgba(255, 206, 86,0.5)',
              'rgba(75, 192, 192,0.5)',
              'rgba(153, 102, 255,0.5)',
              'rgba(255, 159, 64,0.5)'
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
          }]
        },
        options: {},
        plugins: {
            datalabels: {
              anchor: 'end',
              align: 'top',
              formatter: Math.round,
              font: {
                weight: 'bold'
              }
            }
          }
      });
    },
    renderCampaignAdCountChart() {
      const ctx = document.getElementById('campaignAdCountChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.campaignAdCountData.map(data => data.campaignName),
          datasets: [{
            label: 'Ad Count',
            data: this.campaignAdCountData.map(data => data.adCount),
            backgroundColor: 'rgba(255, 159, 64, 0.7)',
            borderColor: 'rgba(255, 159, 64, 1)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    }
  },
  created() {
    this.fetchData();
  }
};
</script>

<style>
.stats-container {
  display: flex;
  justify-content: space-around;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 10px;
  margin-bottom: 20px;
}
.charts-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.chart-card {
  flex: 1 1 calc(50% - 20px);
  padding: 20px;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  height:300px
}
</style>
