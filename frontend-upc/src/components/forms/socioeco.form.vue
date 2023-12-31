<script setup>
	import { ref, reactive, onMounted } from "vue";
	import { useRoute } from "vue-router";
	import Swal from "sweetalert2";
	const route = useRoute();

	const requiredFields = ["¿Cuánto es el ingreso familiar?"];

	const fieldsWithOptions = [
		"Ocupación",
		"Estrato",
		"Tipo de vivienda",
		"¿Recibe ingresos mensualmente?",
		"Acudiente",
		"Nivel académico",
		"¿Cuánto es el ingreso familiar?",
		"Posee computador",
		"Tiene acceso a Internet",
		"Tiene celular smart",
		"Tiene plan de datos",
		"¿Ingresos por trabajar?",
	];

	const dataInscri = reactive({
		Ocupación: {
			options: {
				1: "Únicamente estudiante",
				2: "Empleado",
				3: "Independiente",
				4: "Trabaja medio tiempo",
				5: "Trabaja tiempo completo",
			},
		},
		Estrato: {
			options: {
				1: 1,
				2: 2,
				3: 3,
				4: 4,
				5: 5,
			},
		},
		"Tipo de vivienda": {
			options: {
				1: "Familiar",
				2: "Propia",
				3: "Arrendada",
				4: "Otra",
			},
		},
		"¿Recibe ingresos mensualmente?": {
			options: {
				1: "Sí",
				2: "No",
			},
		},
		Acudiente: {
			options: {
				1: "Sí",
				2: "No",
			},
		},
		"Nivel académico": {
			options: {
				1: "Bachiller",
				2: "Técnico",
				3: "Técnico Bachiller",
				4: "Tecnologo",
				5: "Universitario",
			},
		},
		"¿Cuánto es el ingreso familiar?": {
			value: 0,
			type: "number",
		},
		"Posee computador": {
			options: {
				1: "Sí",
				2: "No",
			},
		},
		"Tiene acceso a Internet": {
			options: {
				1: "Sí",
				2: "No",
			},
		},
		"Tiene celular smart": {
			options: {
				1: "Sí",
				2: "No",
			},
		},
		"Tiene plan de datos": {
			options: {
				1: "Sí",
				2: "No",
			},
		},
		"¿Ingresos por trabajar?": {
			options: {
				1: "Sí",
				2: "No",
			},
		},
	});

	const selectedOption = reactive({});

	const toggleDropdown = (groupKey) => {
		dataInscri[groupKey].isOpen = !dataInscri[groupKey].isOpen;
	};

	const selectOption = (groupKey, option) => {
		selectedOption[groupKey] = option;
		dataInscri[groupKey].isOpen = false;
		setDataTo(groupKey, option);
	};

	const setDataTo = (key, value) => {
		dataTo.value[key] = value;
	};

	const dataTo = ref({});
	//Prosps
	const emisorOfWeek = defineEmits(["formSocio", "formEditSoci"]);

	const sendInfoSocio = () => {
		if (validateForm()) {
			emisorOfWeek("formSocio", dataTo);
		}
	};

	//Emitir evento edit
	const sendEditInfoEconomic = () => {
		if (validateForm()) {
			emisorOfWeek("formEditSoci", dataTo);
		}
	};
	//Validation
	const validateForm = () => {
		const areAllRequiredFieldsFilled = requiredFields.every((fieldName) => {
			const value = dataTo.value[fieldName];
			if (value === undefined) {
				Swal.fire({
					icon: "error",
					title: "Oops...",
					text: `Por favor, selecciona una opción válida para "${fieldName}".`,
				});
				return false;
			}
			return true;
		});

		if (!areAllRequiredFieldsFilled) {
			return false;
		}

		const areAllOptionsSelected = fieldsWithOptions.every((fieldName) => {
			const selectedOption = dataTo.value[fieldName];
			if (selectedOption === undefined) {
				Swal.fire({
					icon: "error",
					title: "Oops...",
					text: `Por favor, selecciona una opción válida para "${fieldName}".`,
				});
				return false;
			}
			return true;
		});

		if (!areAllOptionsSelected) {
			return false;
		}

		return true;
	};

	//Props
	const props = defineProps({
		contendEconomic: {
			type: Object,
		},
	});

	const onContendPersonarlChange = () => {
		dataTo.value = props.contendEconomic.datasSoci;
	};

	onMounted(() => {
		if (route.query.id) {
			onContendPersonarlChange();
		}
	});
</script>

<template>
	<section>
		<div class="mt-10 sm:mt-0">
			<div class="flex flex-col justify-between items-center">
				<div class="">
					<div class="px-4 sm:px-6 flex justify-center items-center flex-col">
						<h3 class="text-3xl font-bold leading-6 text-gray-900">
							Información Socioeconómica
						</h3>
						<p class="mt-2 text-base text-gray-600">
							Complete todos los datos.
						</p>
					</div>
				</div>
				<div class="mt-4 w-full">
					<form>
						<div class="overflow-hidden shadow sm:rounded-md">
							<div class="bg-gray-50 px-4 py-5 sm:p-6">
								<div class="grid gap-4 mb-4 grid-cols-3">
									<div v-for="(group, groupKey) in dataInscri" :key="groupKey">
										<label
											for="Nombres"
											class="block mb-2 text-base font-bold text-gray-900 dark:text-dark">
											{{ groupKey }}
										</label>
										<input
											v-if="group.value === 0"
											:type="group.type"
											required
											v-model="dataTo[groupKey]"
											class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm" />
										<div class="flex" v-if="group.value != 0">
											<button
												id="dropdownDefaultButton"
												@click="toggleDropdown(groupKey)"
												class="w-full border border-gray-300 bg-white shadow-sm text-whit focus:outline-none focus:ring-blue-300 font-medium rounded-md text-sm px-5 py-2 justify-between inline-flex items-center"
												type="button">
												{{
													selectedOption[groupKey] ||
													dataTo[groupKey] ||
													"Seleccionar"
												}}
												<svg
													class="w-2.5 h-2.5 ml-2.5"
													aria-hidden="true"
													xmlns="http://www.w3.org/2000/svg"
													fill="none"
													viewBox="0 0 10 6">
													<path
														stroke="currentColor"
														stroke-linecap="round"
														stroke-linejoin="round"
														stroke-width="2"
														d="m1 1 4 4 4-4" />
												</svg>
											</button>
											<!-- Dropdown menu -->
											<div
												id="dropdown"
												:class="{ hidden: !group.isOpen }"
												class="z-10 bg-white divide-y divide-gray-100 rounded-lg shadow w-60 absolute mt-11"
												style="max-height: 180px; overflow-y: auto">
												<ul
													class="py-2 text-sm text-gray-700"
													aria-labelledby="dropdownDefaultButton">
													<li
														v-for="(data, id) in group.options"
														:key="id"
														class="h-10">
														<h3
															class="block px-4 py-2 hover:bg-gray-100 text-center"
															@click="selectOption(groupKey, data)">
															{{ data }}
														</h3>
													</li>
												</ul>
											</div>
										</div>
									</div>
								</div>
							</div>
							<div
								v-if="!route.query.id"
								class="w-full flex justify-end bg-gray-50">
								<!--                 <button
                  type="button"
                  class="text-white w-44 text-center mb-10 ml-20 bg-gray-800 hover:bg-gray-900 focus:outline-none focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-base py-2.5"
                >
                  Atrás
                </button> -->
								<button
									@click.prevent="sendInfoSocio()"
									type="button"
									class="text-gray-200 mb-10 mr-20 bg-gray-900 hover:bg-gray-700 focus:ring-4 focus:ring-blue-300 font-bold rounded-lg text-base px-5 py-2.5">
									Siguiente
								</button>
							</div>

							<div
								v-if="route.query.id"
								class="w-full flex justify-end bg-gray-50">
								<button
									@click.prevent="sendEditInfoEconomic()"
									type="button"
									class="text-gray-200 mb-10 mr-20 bg-gray-900 hover:bg-gray-700 focus:ring-4 focus:ring-blue-300 font-bold rounded-lg text-base px-5 py-2.5">
									Siguiente
								</button>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	</section>
</template>
