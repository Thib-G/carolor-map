<template>
  <div class="map" ref="map">
  </div>
</template>

<script>
// @ is an alias to /src
import 'leaflet/dist/leaflet.css';

import L from 'leaflet';

import { mapBoxKey } from '@/assets/keys';
import CarolorService from '@/services/carolor-service';

// eslint-disable-next-line
delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  // eslint-disable-next-line
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  // eslint-disable-next-line
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  // eslint-disable-next-line
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});


export default {
  name: 'carolormap',
  data() {
    return {
      carolorService: CarolorService,
      partners: [],
      map: {},
      zoom: 12,
      charleroiLatLng: L.latLng([50.411652, 4.444540]),
      featureGroupPartners: L.featureGroup(),
      basemaps: {
        dark: L.tileLayer(
          `https://api.mapbox.com/v4/mapbox.dark/{z}/{x}/{y}@2x.png?access_token=${mapBoxKey}`,
          {
            attribution: `&copy; <a href="https://www.mapbox.com/feedback/">Mapbox</a>
                        &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>`,
          },
        ),
        light: L.tileLayer(
          `https://api.mapbox.com/v4/mapbox.light/{z}/{x}/{y}@2x.png?access_token=${mapBoxKey}`,
          {
            attribution: `&copy; <a href="https://www.mapbox.com/feedback/">Mapbox</a>
                        &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>`,
          },
        ),
        streets: L.tileLayer(
          `https://api.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}@2x.png?access_token=${mapBoxKey}`,
          {
            attribution: `&copy; <a href="https://www.mapbox.com/feedback/">Mapbox</a>
                        &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>`,
          },
        ),
        satellite: L.tileLayer(
          `https://api.mapbox.com/v4/mapbox.streets-satellite/{z}/{x}/{y}@2x.png?access_token=${mapBoxKey}`,
          {
            attribution: `&copy; <a href="https://www.mapbox.com/feedback/">Mapbox</a>
                        &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>`,
          },
        ),
      },
    };
  },
  created() {
    this.getAllPartners();
  },
  mounted() {
    this.initMap();
    this.updatePartners();
  },
  watch: {
    partners() {
      this.updatePartners();
    },
  },
  methods: {
    getAllPartners() {
      return this.carolorService.getAllPartners().then((data) => {
        this.partners = data;
      });
    },
    initMap() {
      this.map = L.map(this.$refs.map, {
        center: this.charleroiLatLng,
        zoom: this.zoom,
      });
      this.basemaps.streets.addTo(this.map);
      L.control.layers(this.basemaps).addTo(this.map);
      this.featureGroupPartners.addTo(this.map);
    },
    updatePartners() {
      this.featureGroupPartners.clearLayers();
      const geoJson = L.geoJson(this.partners, {
        onEachFeature: (feature, layer) => {
          const popupHTML = document.createElement('div');
          const p = feature.properties;
          popupHTML.innerHTML = `
            <h4>${p.name}</h4>
            <p>${p.address}, ${p.streetnumber}<br />
               ${p.postcode}, ${p.city}<br />
               ${p.phone}</p>
            <p><a href="${feature.properties.url}" target="_blank">Site</a></p>
          `;
          layer.bindPopup(popupHTML);
        },
      });
      this.featureGroupPartners.addLayer(geoJson);
    },
  },
};
</script>

<style scoped>
  .map {
    width: 100%;
    height: 100%;
  }
</style>
