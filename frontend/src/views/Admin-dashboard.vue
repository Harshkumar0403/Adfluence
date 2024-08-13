<template>
  <div class="dashboard">
      <div class="logo">
      <img src="@/assets/logo1.png" alt="Logo" />
      <span style="font-family:Playwrite GB S;font-weight: 400">Adfluence</span>
    </div>
    <div class="header-buttons">
      
      <button @click="navigateTo('/')">Back</button>
      <button @click="logout">Logout</button>
    </div>
     <h1 style="text-align: center;font-family: 'Headland One, serif;color:#31572c">Admin Dashboard</h1>
    <div class="dashboard-content">
      <div class="sidebar">
        <div class="icon-logo">
          <!-- <img src="@/assets/logo1.png" alt="Logo" class="logo" />
          <span style="font-family:Playwrite GB S;font-weight: 400">Adfluence</span> -->
        </div>
        <div class="nav-buttons">
          <button @click="showAnalytics">Analytics</button>
          <button @click="showCampaignRequest">Campaign Request</button>
          <button @click="showSponsorRequest">Sponsor Request</button>
           <button @click="showAddCampaign">Add Campaign</button>
          <button @click="showInfluencersRequest">Influencers</button>
        </div>
      </div>
      <div class="overflow-scroll">
        <div class="main-content">
        <!-- Content for the second section goes here -->
        <SponsorRequest v-if="showingSponsorRequest" />
        <InfluencerRequest v-if="showingInfluencerRequest" />
        <AddCampaign v-if="showingAddCampaign" />
        <CampaignRequest v-if="showingCampaignRequest" />
        <Analytics v-if="showingAnalytics" />


      </div>
      </div>
      
    </div>
    <Footer />
  </div>
</template>


<script>
import Footer from '@/components/Footer.vue';
import SponsorRequest from  '@/components/SponsorRequest.vue';
import InfluencerRequest from '@/components/InfluencerRequest.vue';
import CampaignRequest from '@/components/CampaignRequest.vue';
import AddCampaign from '@/components/AddCampaign.vue';
import Analytics from '@/components/Analytics.vue'

export default {
  name: 'AdminDashboard',
  components: {
    Footer,
    SponsorRequest,
    InfluencerRequest,
    AddCampaign,
    CampaignRequest,
    Analytics

  },
  data() {
    return {
      currentView: 'CampaignRequests',
      showingSponsorRequest : false,
      showingInfluencerRequest : false,
      showingAddCampaign: false,
      showingCampaignRequest : false,
      showingAnalytics : true,
    };
  },
  methods: {
    logout() {
      // Handle logout logic here
      localStorage.clear();
      this.$router.push('/login');
    },
    showSponsorRequest(){
      this.showingSponsorRequest=true;
      this.showingInfluencerRequest=false;
      this.showingAddCampaign=false;
      this.showingCampaignRequest=false;
      this.showingAnalytics=false;
    },
    showInfluencersRequest(){
      this.showingSponsorRequest=false;
      this.showingInfluencerRequest=true
      this.showingAddCampaign=false;
      this.showingCampaignRequest=false;
      this.showingAnalytics=false;
    },
    showCampaignRequest(){
      this.showingSponsorRequest=false;
      this.showingInfluencerRequest=false;
      this.showingCampaignRequest=true;
      this.showingAddCampaign=false;
      this.showingAnalytics=false;
    },
    showAddCampaign(){
      this.showingSponsorRequest=false;
      this.showingInfluencerRequest=false;
      this.showingAddCampaign=true;
      this.showingCampaignRequest=false;
      this.showingAnalytics=false;
    },
    showAnalytics(){
      this.showingAnalytics=true,
       this.showingSponsorRequest=false;
      this.showingInfluencerRequest=false;
      this.showingAddCampaign=false;
      this.showingCampaignRequest=false;
    }
  }
};
</script>

<style scoped>
.dashboard {
  background-color: #f5ebe0;
  /* height: 100vh; */
  display: flex;
  flex-direction: column;
}
.logo img {
  height: 40px;
  justify-content: flex-start;
}

.header-buttons {
  display: flex;
  justify-content: flex-end;
  padding: 10px;
}

.header-buttons button {
  background-color: #31572c;
  color: #fff;
  border: none;
  padding: 10px;
  margin-left: 10px;
  border-radius: 18px;
  cursor: pointer;
}

.header-buttons button:hover {
  background-color: #805a4a;
}

.dashboard-content {
  display: flex;
  flex: 1;
}

.sidebar {
  width: 20vw;
  background-color: #9f7e69;
  padding: 20px;
  display: flex;
  margin-left:10px;
  flex-direction: column;
  margin-top: 25px;
  justify-content: flex-start;
  border-radius: 18px;
  height: 150 vh;
}

.nav-buttons button {
  background-color: #31572c;
  color: #fff;
  border: none;
  padding: 10px;
  margin: 10px 0;
  border-radius: 18px;
  cursor: pointer;
  width: 100%;
}

.nav-buttons button:hover {
  background-color: #ddd;
}

.main-content {
  width: 80vw;
  margin: 20px;
  padding: 20px;
  border-radius: 18px;
  background-color: white;
  height: 120vh;
  overflow: scroll;
  scrollbar-color: orange grey;
  scrollbar-width: thin;
}

.badge {
  background-color: red;
  color: white;
  border-radius: 50%;
  padding: 5px;
  font-size: 12px;
}

</style>
