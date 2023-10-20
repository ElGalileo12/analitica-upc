<script setup>
	import { ref, reactive, onMounted } from "vue";
	import { useRoute } from "vue-router";
	import Swal from "sweetalert2";
	const route = useRoute();

	const requiredFields = [
		"Semestre de inicio",
		"Semestre Cursados",
		"Promedio Acumulado",
		"Año de finalizacion pregrado",
		"Año de grado",
	];

	const fieldsWithOptions = [
		"Titulo",
		"¿Domina una segunda lengua?",
		"¿Cuál nivel?",
		"¿Hizo practicas?",
		"¿Tiene estudios de postgrados?",
		"Último estudio de posgrado",
		"Nivel del posgrado",
	];

	const dataInscri = reactive({
		Titulo: {
			options: {
				1: "Ing. Electronica",
				2: "Ing. Electronica",
				3: "Ing. Electronica",
			},
		},
		"Semestre de inicio": {
			value: 0,
			type: "text",
		},
		"Semestre Cursados": {
			value: 0,
			type: "number",
		},
		"Promedio Acumulado": {
			value: 0,
			type: "number",
		},
		"Año de finalizacion pregrado": {
			value: 0,
			type: "text",
		},
		"Año de grado": {
			value: 0,
			type: "text",
		},
		"¿Domina una segunda lengua?": {
			options: {
				1: "Si",
				2: "No",
			},
		},
		"¿Cuál nivel?": {
			options: {
				1: "A1",
				2: "A2",
				3: "B1",
				4: "B2",
				5: "C1",
				6: "C2",
			},
		},
		"¿Hizo practicas?": {
			options: {
				1: "Si",
				2: "No",
			},
		},
		"¿Tiene estudios de postgrados?": {
			options: {
				1: "Si",
				2: "No",
			},
		},
		"Último estudio de posgrado": {
			options: {
				1: "Especialización",
				2: "Maestría",
				3: "Doctorado",
				4: "Pos-Doctorado",
				5: "Ninguno",
			},
		},
		"Nivel del posgrado": {
			options: {
				1: "Nacional",
				2: "Extranjera",
				3: "Ninguno",
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
	const emisorOfWeek = defineEmits(["formAcademico", "formEditAcademico"]);

	const sendInfoAcademic = () => {
		if (validateForm()) {
			emisorOfWeek("formAcademico", dataTo);
		}
	};
	//Emitir evento edit
	const sendEditAcademic = () => {
		if (validateForm()) {
			emisorOfWeek("formEditAcademico", dataTo);
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
		contendAcademic: {
			type: Object,
		},
	});

	const onContendPersonarlChange = () => {
		dataTo.value = props.contendAcademic.datasAcad;
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
							Información Academica
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
								<div class="grid gap-6 mb-4 grid-cols-3">
									<div v-for="(group, groupKey) in dataInscri" :key="groupKey">
										<label
											for="Nombres"
											class="block mb-2 text-base font-bold text-gray-900 dark:text-white px-2">
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
												class="w-full border border-gray-300 bg-white shadow-sm text-whit focus:outline-none focus:ring-blue-300 font-medium rounded-md mt-0 text-sm px-5 py-2 justify-between inline-flex items-center"
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
												class="z-10 bg-white divide-y divide-gray-100 rounded-lg shadow w-96 absolute mt-11"
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
								<button
									@click.prevent="sendInfoAcademic()"
									type="button"
									class="text-gray-200 mb-10 mr-20 bg-gray-900 hover:bg-gray-700 focus:ring-4 focus:ring-blue-300 font-bold rounded-lg text-base px-5 py-2.5">
									Enviar
								</button>
							</div>
							<div
								v-if="route.query.id"
								class="w-full flex justify-end bg-gray-50">
								<button
									@click.prevent="sendEditAcademic()"
									type="button"
									class="text-gray-200 mb-10 mr-20 bg-gray-900 hover:bg-gray-700 focus:ring-4 focus:ring-blue-300 font-bold rounded-lg text-base px-5 py-2.5">
									Enviar
								</button>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	</section>
</template>
