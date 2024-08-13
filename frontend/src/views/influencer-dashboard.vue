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
    <h1 style="text-align: center;font-family: 'Headland One, serif;color:#31572c">Influencer's Dashboard</h1>
    <div class="dashboard-content">
      <div class="sidebar">
        <div class="icon-logo">
          <!-- <img src="@/assets/logo1.png" alt="Logo" class="logo" />
          <span style="font-family:Playwrite GB S;font-weight: 400">Adfluence</span> -->
        </div>
        <div class="nav-buttons">
          <button @click="showProfile">Profile</button>
          <button @click="showsponsors">Brands</button>
          <button @click="showCampaign">Campaigns</button>
          <button @click="showAdRequest">Ad Requests</button>
          <button @click="showAd">Ads</button>
        </div>
      </div>
      <div class="main-content">
        <!-- Content for the second section goes here -->
         <CaseStudyCards  v-if="defaultcard"/>
         <Profile v-if="showingProfile" />
          <Campaigns  v-if="showingCampaign" />
          <Sponsors v-if="showingSponsors" />
          <AdRequests v-if="showingAdRequests" />
          <AdComponent v-if="showingAd" />
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
import Profile from '@/components/Profile.vue'
import CaseStudyCards from '@/components/CaseStudyCards.vue';
import Campaigns from '@/components/Campaigns.vue';
import Sponsors from '@/components/Sponsors.vue';
import AdRequests from '@/components/AdRequests.vue';
import AdComponent from '@/components/AdComponent.vue';



export default {
  components: {
    Profile,
    Footer,
    CaseStudyCards,
    Campaigns,
    Sponsors,
    AdRequests,
    AdComponent

  },
  data() {
    return {
      showingProfile: false,
      defaultcard :true,
      showingCampaign:false,
      showingSponsors :false,
      showingAdRequests : false,
      showingAd:false,
    };
  },
  methods: {
    showProfile() {
      this.defaultcard = false;
      this.showingProfile = true;
      this.showingSponsors =false;
       this.showingCampaign=false;
       this.showingAdRequests = false;
       this.showingAd=false;
    },
    showCampaign() {
      this.defaultcard = false;
      this.showingProfile = false;
      this.showingCampaign=true;
      this.showingSponsors =false;
      this.showingAdRequests = false;
       this.showingAd=false;
    },
    showsponsors() {
      this.defaultcard = false;
      this.showingProfile = false;
      this.showingCampaign=false;
      this.showingSponsors =true;
      this.showingAdRequests = false;
       this.showingAd=false;
    },
    showAdRequest(){
      this.defaultcard = false;
      this.showingProfile = false;
      this.showingCampaign=false;
      this.showingSponsors = false;
      this.showingAdRequests = true;
       this.showingAd=false;
    },
    showAd() {
      this.defaultcard = false;
      this.showingProfile = false;
      this.showingSponsors = false;
      this.showingCampaign=false;
      this.showingAdRequests = false;
      this.showingAd=true
    },
    navigateTo(page) {
      this.$router.push(`/${page}`);
    },
    logout() {
      localStorage.clear();
      this.$router.push('/login');
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
  width: 18vw;
  background-color: #9f7e69;
  padding: 20px;
  display: flex;
  margin-left:10px;
  flex-direction: column;
  margin-top: 25px;
  justify-content: flex-start;
  border-radius: 18px;
  height: 100 vh;
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
  width: 82vw;
  margin: 20px;
  padding: 20px;
  border-radius: 18px;
  background-color: white;
  height: 120vh;
  overflow: scroll;
  scrollbar-color: red orange;
  scrollbar-width: thin;
}
</style>